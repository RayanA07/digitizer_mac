# LinePilot Digitizer on macOS

The Mac app is the **same code** as the Windows app, built for macOS. Every menu, button and
option works the same way, so the main guides apply as written:

- **[README](../README.md)** — screenshot walkthrough of the app, start to finish.
- **[Digitizer/README.md](README.md)** — the full reference: every menu, CLI option and error message.

This page covers only what is different on a Mac: installing it, the keys and paths that change,
setting up the command line, and building the app yourself.

---

## Install the app (no Python needed)

**Requirements:** macOS 15 Sequoia or newer, on an Apple Silicon or Intel Mac.

1. **Find out which chip your Mac has.** Apple menu → **About This Mac**.
   - **Chip: Apple M1, M2, M3, M4…** → you need the **AppleSilicon** download.
   - **Processor: …Intel…** → you need the **Intel** download.
2. Open the **[latest release](https://github.com/RayanA07/digitizer_mac/releases/latest)**, scroll to
   **Assets**, and download `Digitizer-<version>-macOS-AppleSilicon.zip` or
   `Digitizer-<version>-macOS-Intel.zip`. (Ignore the *Source code* links.)
3. Double-click the zip in **Downloads** to unpack **`Digitizer.app`**. Drag it into
   **Applications** if you like — there is nothing else to install. The Tesseract OCR engine
   that reads axis numbers is bundled inside the app.

### First launch: "Apple could not verify…" (expected, once)

The app isn't signed with a paid Apple Developer ID, so macOS blocks the very first launch.
This is not a virus warning.

1. Double-click `Digitizer.app`. When macOS says it can't verify the app, click **Done**.
2. Open **System Settings → Privacy & Security**, scroll down to *"Digitizer" was blocked…*,
   and click **Open Anyway**. Confirm with your password or Touch ID.

From then on it opens with a normal double-click.

> **"Digitizer is damaged and can't be opened"** means the download's quarantine flag is
> stuck. In **Terminal** run the line below (adjust the path if the app isn't in
> Applications), then open it again:
>
> ```bash
> xattr -dr com.apple.quarantine /Applications/Digitizer.app
> ```

> **"You can't use this version of the application with this version of macOS"** means the
> Mac is older than the build supports (see Requirements). Run from source instead (below) —
> that works on older macOS too.

The optional **Accuracy Tester** installs the same way from
`AccuracyTester-<version>-macOS-<chip>.zip`.

---

## What's different from the Windows instructions

When a guide says… | …on a Mac it is
--- | ---
`Digitizer.exe` | `Digitizer.app`
**Ctrl+Z** (undo a calibration click) | **⌘Z** — the app's own hints already say ⌘Z
**Esc** (leave manual mask mode), **Shift+click** (remove a mask) | the same keys
File Explorer / *Open in Terminal* | Finder / **New Terminal at Folder** (see below)
PowerShell | **Terminal** (⌘ + Space, type *Terminal*)
`py digitizer.py …` | `python3 digitizer.py …`
`C:\Users\you\Downloads\graph.png` | `~/Downloads/graph.png`
Error log in `%LOCALAPPDATA%\DataDigitizer\<version>\logs` | `~/Library/Application Support/DataDigitizer/<version>/logs` (or **Advanced → Error Log** in the app)
SmartScreen / Smart App Control | Gatekeeper — see *First launch* above

The **Import, Tools, Advanced, Export** and **About ▾** menus are buttons inside the app
window, exactly as in the screenshots — they don't move to the Mac menu bar at the top of
the screen.

The command line's own `--help`, `template` and error messages already print the Mac
versions of every command and path.

---

## The command line

> **The `.app` is not the command line.** `Digitizer.app` is the graphical program; it
> doesn't contain `digitizer.py` and ignores command-line options. Running
> `python3 digitizer.py` inside the app gives *No such file or directory* — that's
> expected. The command line runs from the **source code** with Python.

### One-time setup (~5 minutes)

Open **Terminal** (⌘ + Space, type `Terminal`, Enter) and:

**1. Install Homebrew** (skip if `brew --version` already works), then close and reopen Terminal:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**2. Install Python and Tesseract** (the OCR engine the source code calls):

```bash
brew install python tesseract
```

**3. Download the source code.** On the [repository page](https://github.com/RayanA07/digitizer_mac)
click the green **Code** button → **Download ZIP**, then double-click the zip in Downloads.
You get a folder named `digitizer_mac-main`. *(Or: `git clone https://github.com/RayanA07/digitizer_mac.git`.)*

**4. Make a private Python environment and install the libraries.** Homebrew's Python
refuses system-wide `pip install` (*"externally-managed-environment"*), so give the
project its own:

```bash
cd ~/Downloads/digitizer_mac-main/Digitizer
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Check you're in the right folder — `ls digitizer.py` must list the file.

### Every time after that

```bash
cd ~/Downloads/digitizer_mac-main/Digitizer
source .venv/bin/activate
python3 digitizer.py ~/Downloads/graph.png
```

Everything in **[Digitizer/README.md → Using the command line](README.md#using-the-command-line)**
then works with `python3` in place of `py`. A few Mac examples:

```bash
python3 digitizer.py graph.png --verbose 1                       # full detail + log file
python3 digitizer.py graph.png --axis 0,10,0,100 --out ~/Desktop/out
python3 digitizer.py 'digitizer_cli(pic_dir="/Users/you/Downloads/graph.png", color=(255,0,0))'
python3 digitizer.py ~/Downloads/charts                          # a whole folder (batch mode)
python3 digitizer.py template                                    # fill-in-the-blank template
python3 digitizer_2_11.py                                        # open the app from source
```

> Inside the quoted `digitizer_cli(...)` form, write paths out in full (`/Users/you/...`) —
> the shell doesn't expand `~` inside quotes.

**Shortcut:** in Finder, right-click (Control-click) the `Digitizer` folder → **New Terminal
at Folder**. If it's missing, turn it on in **System Settings → Keyboard → Keyboard
Shortcuts → Services → Files and Folders**.

### Scoring results (Accuracy Tester CLI)

```bash
cd ~/Downloads/digitizer_mac-main/AccuracyTester
python3 -m pip install -r requirements.txt      # inside the same .venv
python3 accuracy_batch_cli.py --digitized-dir ~/Downloads/charts/digitized_csvs --ground-truth-dir ~/Desktop/truth
```

---

## Build the app yourself

macOS apps have to be built on a Mac. With Homebrew installed, from the repository folder:

```bash
brew install tesseract dylibbundler
bash Digitizer/build_macos.sh           # -> Digitizer/dist/Digitizer.app + zip
bash AccuracyTester/build_macos.sh      # -> AccuracyTester/dist/AccuracyTester.app + zip
```

`build_macos.sh` installs the Python libraries, makes the icon from the Windows `.ico`,
copies a self-contained Tesseract (binary, libraries, English language data) into
`vendor/tesseract`, runs PyInstaller with `digitizer_macos.spec`, records the minimum
macOS in `Info.plist`, ad-hoc signs the app and zips it.

The result runs on the **same chip** as the Mac that built it, and on **that Mac's macOS
version or newer**. That's because the bundled Tesseract comes from Homebrew, which compiles
for the build machine's macOS (`python3 tools/macho_minos.py dist/Digitizer.app --report`
shows which file sets the limit). The release workflow therefore builds on the oldest
supported runner, once per chip.

### How each release is checked

`.github/workflows/macos-release.yml` runs on every push, on an Apple Silicon **and** an
Intel macOS 15 runner:

1. Both unit-test suites, a check that no Windows-only text appears in `--help`, and an
   end-to-end smoke test (render charts → batch-digitize with OCR → score against the
   true data).
2. Builds both apps and checks that `Info.plist` matches `version.json`.
3. **Uninstalls the runner's own Tesseract**, then runs the *built* `Digitizer.app` on a
   real Raman spectrum (`LINEPILOT_SELFTEST`): the axes must be read by the app's bundled
   OCR and the curve must match the ground truth within 2 % of its range.
4. Launches both apps and checks that they stay open.
5. On a `v*` tag, attaches all four zips to one release.

---

## Troubleshooting (Mac-specific)

**OCR says "Tesseract OCR executable not found" when running from source.**
Run `brew install tesseract`, then open a new Terminal window. To use a specific copy:
`export TESSERACT_CMD=/opt/homebrew/bin/tesseract`. The downloaded `.app` never needs this.

**`pip install` fails with "externally-managed-environment".**
You skipped the `.venv` step — run `python3 -m venv .venv` and `source .venv/bin/activate` first.

**`python3: command not found`.** Run `brew install python`, then open a new Terminal window.

**`zsh: no matches found` with the `digitizer_cli(...)` form.** Keep the single quotes around
the whole `'digitizer_cli(...)'` call — zsh treats unquoted brackets as file patterns.

**Where is the error log?** `~/Library/Application Support/DataDigitizer/<version>/logs`
— in Finder use **Go → Go to Folder…** and paste that path. Or use **Advanced → Error Log**
in the app.

For everything else (wrong colors, wrong axis numbers, export does nothing, batch pairing)
see **[Digitizer/README.md → Troubleshooting](README.md#troubleshooting)** — the fixes are
the same on a Mac.
