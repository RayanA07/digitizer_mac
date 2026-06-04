from __future__ import annotations

import os
import shutil
import stat
import subprocess
import sys
import threading
from pathlib import Path
from tkinter import BOTH, BOTTOM, DISABLED, LEFT, NORMAL, RIGHT, X, Button, Frame, Label, StringVar, Tk, messagebox
from tkinter import ttk


APP_VERSION = "2.11.mac"
INSTALL_DIR = Path.home() / "Applications" / "Data Digitizer"
DESKTOP_DIR = Path.home() / "Desktop"

PAYLOADS = [
    {
        "name": "Digitizer",
        "source": "Digitizer.app",
        "destination": "Digitizer.app",
        "kind": "app",
    },
    {
        "name": "AccuracyTester",
        "source": "AccuracyTester.app",
        "destination": "AccuracyTester.app",
        "kind": "app",
    },
    {
        "name": "datadigitizer CLI",
        "source": "datadigitizer",
        "destination": "datadigitizer",
        "kind": "file",
    },
]


def resource_root() -> Path:
    return Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))


def payload_roots() -> list[Path]:
    roots = [resource_root() / "payload"]
    executable = Path(sys.executable).resolve()
    for parent in executable.parents:
        roots.append(parent / "payload")
        if parent.name == "Contents":
            roots.append(parent / "Frameworks" / "payload")
            roots.append(parent / "Resources" / "payload")
            break
    roots.append(Path(__file__).resolve().parent / "payload")
    seen: set[Path] = set()
    unique_roots: list[Path] = []
    for root in roots:
        if root not in seen:
            unique_roots.append(root)
            seen.add(root)
    return unique_roots


def resolve_payload(name: str) -> Path | None:
    for root in payload_roots():
        direct = root / name
        if direct.exists():
            return direct
        if root.exists():
            for candidate in root.rglob(name):
                if candidate.exists():
                    return candidate
    return None


def copy_tree_with_progress(source: Path, destination: Path, progress_callback) -> None:
    files = [path for path in source.rglob("*") if path.is_file()]
    total = sum(path.stat().st_size for path in files) or 1
    copied = 0
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True, exist_ok=True)
    for path in source.rglob("*"):
        relative = path.relative_to(source)
        target = destination / relative
        if path.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        copied += path.stat().st_size
        progress_callback(copied, total)


def copy_file_with_progress(source: Path, destination: Path, progress_callback) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    total = source.stat().st_size or 1
    copied = 0
    with source.open("rb") as src, destination.open("wb") as dst:
        while True:
            chunk = src.read(1024 * 1024)
            if not chunk:
                break
            dst.write(chunk)
            copied += len(chunk)
            progress_callback(copied, total)
    mode = destination.stat().st_mode
    destination.chmod(mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def remove_quarantine(path: Path) -> None:
    subprocess.run(
        ["xattr", "-dr", "com.apple.quarantine", str(path)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )


def make_desktop_symlink(name: str, target: Path) -> None:
    DESKTOP_DIR.mkdir(parents=True, exist_ok=True)
    link = DESKTOP_DIR / name
    if link.is_symlink() or link.exists():
        if link.is_dir() and not link.is_symlink():
            shutil.rmtree(link)
        else:
            link.unlink()
    link.symlink_to(target)


def make_cli_command() -> None:
    command = DESKTOP_DIR / "DataDigitizer CLI.command"
    command.write_text(
        "\n".join(
            [
                "#!/bin/zsh",
                f"cd {shell_quote(str(INSTALL_DIR))}",
                "./datadigitizer",
                "echo",
                "echo 'Use the command shown above with digitizer_cli(...) for one-line runs.'",
                "echo 'Press Return to close.'",
                "read",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    command.chmod(command.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    remove_quarantine(command)


def shell_quote(value: str) -> str:
    return "'" + value.replace("'", "'\\''") + "'"


class InstallerApp:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Data Digitizer 2.11.mac Installer")
        self.root.geometry("560x240")
        self.root.resizable(False, False)

        self.status = StringVar(value="Ready to install Data Digitizer 2.11.mac.")
        self.detail = StringVar(value="Installs Digitizer.app, AccuracyTester.app, and the datadigitizer CLI.")

        outer = Frame(self.root, padx=18, pady=16)
        outer.pack(fill=BOTH, expand=True)

        Label(outer, text="Data Digitizer 2.11.mac", font=("Helvetica", 18, "bold")).pack(anchor="w")
        Label(outer, textvariable=self.status, font=("Helvetica", 11)).pack(anchor="w", pady=(12, 0))
        Label(outer, textvariable=self.detail, font=("Helvetica", 10), fg="#555555").pack(anchor="w", pady=(4, 10))

        self.progress = ttk.Progressbar(outer, orient="horizontal", mode="determinate", maximum=100)
        self.progress.pack(fill=X, pady=(4, 16))

        button_row = Frame(outer)
        button_row.pack(side=BOTTOM, fill=X)

        self.install_button = Button(button_row, text="Install", width=14, command=self.start_install)
        self.install_button.pack(side=LEFT)

        self.open_button = Button(button_row, text="Open Digitizer", width=16, command=self.open_digitizer, state=DISABLED)
        self.open_button.pack(side=LEFT, padx=(8, 0))

        self.close_button = Button(button_row, text="Close", width=12, command=self.root.destroy)
        self.close_button.pack(side=RIGHT)

    def set_progress(self, value: float, status: str | None = None, detail: str | None = None) -> None:
        def update() -> None:
            self.progress["value"] = max(0, min(100, value))
            if status is not None:
                self.status.set(status)
            if detail is not None:
                self.detail.set(detail)

        self.root.after(0, update)

    def start_install(self) -> None:
        self.install_button.configure(state=DISABLED)
        self.open_button.configure(state=DISABLED)
        threading.Thread(target=self.install, daemon=True).start()

    def install(self) -> None:
        try:
            INSTALL_DIR.mkdir(parents=True, exist_ok=True)

            for index, payload in enumerate(PAYLOADS):
                source = resolve_payload(payload["source"])
                if source is None:
                    raise RuntimeError(f"Missing installer payload: {payload['source']}")
                destination = INSTALL_DIR / payload["destination"]
                base = index * 72 / len(PAYLOADS)
                span = 72 / len(PAYLOADS)
                self.set_progress(base, f"Installing {payload['name']}...", str(destination))
                if payload["kind"] == "app":
                    copy_tree_with_progress(
                        source,
                        destination,
                        lambda done, total, b=base, s=span: self.set_progress(b + (done / total) * s),
                    )
                else:
                    copy_file_with_progress(
                        source,
                        destination,
                        lambda done, total, b=base, s=span: self.set_progress(b + (done / total) * s),
                    )
                remove_quarantine(destination)

            self.set_progress(80, "Creating Desktop shortcuts...", str(DESKTOP_DIR))
            make_desktop_symlink("Digitizer.app", INSTALL_DIR / "Digitizer.app")
            make_desktop_symlink("AccuracyTester.app", INSTALL_DIR / "AccuracyTester.app")
            make_cli_command()

            self.set_progress(100, "Data Digitizer 2.11.mac installed successfully.", f"Installed to {INSTALL_DIR}")
            self.root.after(0, lambda: self.open_button.configure(state=NORMAL))
            self.root.after(0, lambda: messagebox.showinfo("Install complete", "Desktop shortcuts were created for Digitizer, AccuracyTester, and DataDigitizer CLI."))
        except Exception as exc:
            self.set_progress(0, "Install failed.", str(exc))
            self.root.after(0, lambda: self.install_button.configure(state=NORMAL))
            self.root.after(0, lambda: messagebox.showerror("Install failed", str(exc)))

    def open_digitizer(self) -> None:
        digitizer = INSTALL_DIR / "Digitizer.app"
        if not digitizer.exists():
            messagebox.showerror("Missing app", f"Could not find {digitizer}")
            return
        subprocess.Popen(["open", str(digitizer)])

    def run(self) -> None:
        self.root.mainloop()


def main() -> int:
    InstallerApp().run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
