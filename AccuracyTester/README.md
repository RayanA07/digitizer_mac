# Accuracy Tester (macOS)

A standalone desktop tool that compares a digitized CSV against a reference
("original") CSV and reports accuracy metrics. Independent of the Digitizer app.

## Run the app (no Python needed)

Download `AccuracyTester-macos.app.zip` from the
[Releases page](https://github.com/RayanA07/digitizer_mac/releases), double-click
the zip to unpack `AccuracyTester.app`, then double-click the app.

On first launch macOS Gatekeeper may say the app is from an "unidentified
developer". Right-click (or Control-click) `AccuracyTester.app`, choose **Open**,
then **Open** again — or allow it under **System Settings → Privacy & Security →
Open Anyway**.

## Run from source

```bash
python3 -m pip install -r requirements.txt
python3 accuracytester_desktop.py
```

Load two CSV files (original vs digitized). Drag-and-drop works when `tkinterdnd2`
is installed; otherwise click the panels to browse for files.

## Build the macOS app

macOS apps must be built on a Mac:

```bash
bash build_macos.sh
```

Output: `dist/AccuracyTester.app` (and `dist/AccuracyTester-macos.app.zip`) — a
windowed app you double-click to open. No Tesseract is needed for this tool.

## Folder contents

```text
AccuracyTesterPro.py        # The tool (Tkinter + matplotlib + pandas)
accuracytester_desktop.py   # Entry point
accuracytester_macos.spec   # PyInstaller spec (AccuracyTester.app)
build_macos.sh              # macOS build script
make_macos_icons.py         # Builds assets/accuracytester.icns from a source image
requirements.txt            # Python dependencies
version.json                # App name + version
assets/                     # Application icon source
```
