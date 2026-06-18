# Data Digitizer 2.12 (macOS)

macOS Tahoe build of Data Digitizer 2.12.

## Downloads

- **`Digitizer-macos.app.zip`** — the main Data Digitizer app (`Digitizer.app`). Double-click the zip to unpack `Digitizer.app`. Tesseract OCR is bundled inside the app, so axis detection and masking work with no extra install.
- **`AccuracyTester-macos.app.zip`** — the optional Accuracy Tester app (`AccuracyTester.app`) for comparing a digitized CSV against a reference CSV.

## Just want to digitize a graph? Double-click `Digitizer.app`

These downloads are the **graphical apps** — open them and follow the on-screen steps. No Python, no terminal, nothing to install.

## Want the command line (`python3 digitizer.py ...`)?

The `.app` is **not** the command line and does **not** contain `digitizer.py` — running `python3 digitizer.py` *inside* `Digitizer.app` gives `No such file or directory`, which is expected. The CLI runs from the **source code** (a separate download) with Python + Tesseract. See **["Set up the command line from scratch" in the README](https://github.com/RayanA07/digitizer_mac#set-up-the-command-line-from-scratch-one-time-5-minutes)** for the full step-by-step.

## Opening the apps (Gatekeeper)

These builds are ad-hoc signed, not Apple Developer ID notarized. The first time you open one, macOS may say:

> "Digitizer.app" cannot be opened because it is from an unidentified developer.

To open it anyway:

1. **Right-click** (or Control-click) `Digitizer.app` and choose **Open**, then click **Open** again in the dialog, **or**
2. Open **System Settings → Privacy & Security**, scroll to the message about the blocked app, and click **Open Anyway**.

You only need to do this once per app.

If macOS reports the app as "damaged", clear the quarantine flag in Terminal:

```bash
xattr -dr com.apple.quarantine "$HOME/Downloads/Digitizer.app"
xattr -dr com.apple.quarantine "$HOME/Downloads/AccuracyTester.app"
```

## Build

- Built on the GitHub Actions `macos-26` (macOS Tahoe) runner with Python 3.11 and PyInstaller.
- Both apps are produced by `Digitizer/build_macos.sh` and `AccuracyTester/build_macos.sh`.
