# Data Digitizer 2.11.mac

macOS Tahoe release packaging for Data Digitizer 2.11.

This repo contains the macOS release wrapper and packaging around the existing digitizer algorithms:

- `DataDigitizer Installer.app` windowed installer
- `Digitizer.app` desktop GUI
- `AccuracyTester.app` desktop GUI
- `datadigitizer` CLI executable
- bundled Tesseract OCR runtime for Digitizer OCR features

The digitizer algorithm modules are carried forward from 2.11. macOS-specific work lives in wrapper, installer, packaging, and build files.

## Easiest Mac Install

Go to the release page:

https://github.com/RayanA07/digitizer_mac/releases/tag/v2.11.mac

Recommended download:

```text
DataDigitizer-2.11.mac-Installer.app.zip
```

Then:

1. Open **Downloads** in Finder.
2. Double-click `DataDigitizer-2.11.mac-Installer.app.zip`.
3. Right-click or Control-click `DataDigitizer Installer.app`.
4. Click **Open**.
5. If macOS warns about an unidentified developer, click **Open** again.
6. Click **Install** in the installer window.

The installer copies files to:

```text
~/Applications/Data Digitizer
```

It also creates Desktop launchers for:

- `Digitizer.app`
- `AccuracyTester.app`
- `DataDigitizer CLI.command`

No Python, Homebrew, Tesseract, or VS Code is needed for normal app use.

## Gatekeeper Fix

These builds are ad-hoc signed, not Apple Developer ID notarized. If macOS says the installer or app is damaged, open Terminal and run:

```bash
xattr -dr com.apple.quarantine "$HOME/Downloads/DataDigitizer Installer.app"
```

If the app is already installed and blocked:

```bash
xattr -dr com.apple.quarantine "$HOME/Applications/Data Digitizer/Digitizer.app"
xattr -dr com.apple.quarantine "$HOME/Applications/Data Digitizer/AccuracyTester.app"
xattr -dr com.apple.quarantine "$HOME/Applications/Data Digitizer/datadigitizer"
```

Then right-click or Control-click the app and choose **Open**.

## CLI Quick Start

After installing, open Terminal and run:

```bash
"$HOME/Applications/Data Digitizer/datadigitizer" 'digitizer_cli(pic_dir="/Users/yourname/Downloads/Example 2.png", output_dir="/Users/yourname/Downloads/testcli")'
```

Auto mode with blank optional fields:

```bash
"$HOME/Applications/Data Digitizer/datadigitizer" 'digitizer_cli(pic_dir="/Users/yourname/Downloads/Example 2.png", , , , output_dir="/Users/yourname/Downloads/testcli")'
```

Manual mode:

```bash
"$HOME/Applications/Data Digitizer/datadigitizer" 'digitizer_cli(pic_dir="/Users/yourname/Downloads/Example 2.png", color=(255,0,0), tick_setting=([10,200],[500,200],[10,200],[10,20]), axis_values=(0,10,0,100), output_dir="/Users/yourname/Downloads/testcli")'
```

CLI inputs:

- `pic_dir`: image file path, required.
- `color`: graph line color as RGB, blank or `null` means auto color.
- `tick_setting`: four pixel coordinates, blank or `null` means OCR/auto calibration.
- `axis_values`: Xmin, Xmax, Ymin, Ymax, blank or `null` means OCR.
- `output_dir`: folder where results save. Blank saves beside the image.

CLI output:

```text
Pipeline done. Output data to /Users/.../Example 2_digitized_points.csv. Points: 201.
Overlapping plot: /Users/.../Example 2_digitized_overlay.png
```

It creates:

- `<image>_digitized_points.csv`
- `<image>_digitized_overlay.png`

## Copying File Paths On Mac

Finder path copy:

1. Open Finder.
2. Find the graph image.
3. Right-click or Control-click the image.
4. Hold the **Option** key.
5. Click **Copy "<filename>" as Pathname**.
6. Paste that path between the double quotes after `pic_dir=`.

Example:

```bash
pic_dir="/Users/aakashsjoshi/Downloads/Example 2.png"
```

If you drag a file into Terminal, macOS may insert backslash-escaped spaces like `Example\ 2.png`. The CLI tolerates that for macOS paths.

## Source Build On macOS

macOS apps must be built on macOS. From a Mac:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-macos.txt
brew install tesseract dylibbundler
bash scripts/build_macos.sh
```

Outputs are written to:

```text
release/
```

## Source CLI

From a source checkout:

```bash
python3 2.11.py 'digitizer_cli(pic_dir="/Users/yourname/Downloads/Example 2.png", output_dir="/Users/yourname/Downloads/testcli")'
```

Show help:

```bash
python3 2.11.py
```

## GitHub Release Build

The `Build macOS 2.11.mac` workflow builds on the `macos-26` runner and uploads release zips. Pushing tag `v2.11.mac` creates a GitHub Release with generated artifacts.
