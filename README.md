# Data Digitizer 2.11.mac

macOS Tahoe release packaging for Data Digitizer 2.11.

This repository mirrors the Windows 2.11 release shape:

- `Digitizer.app` desktop GUI
- `AccuracyTester.app` desktop GUI
- `datadigitizer` CLI executable with one-line and interactive wizard modes
- bundled Tesseract OCR runtime for Digitizer OCR features

The digitizer algorithm modules are carried forward from 2.11. The macOS-specific work lives in wrapper, packaging, and build files.

## Build On macOS

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

## CLI

Interactive prompt from the released macOS package:

```bash
/Users/aakashsjoshi/Downloads/DataDigitizer-2.11.mac/datadigitizer
```

Or from source:

```bash
python 2.11.py
```

One-line mode:

```bash
./dist/datadigitizer cli \
  --pic-dir /path/to/plot.png \
  --color 255,0,0 \
  --tick-setting "[10,90],[190,90],[10,90],[10,10]" \
  --axis-values 0,10,0,100 \
  --output-dir /path/to/output
```

You can also supply axis bounds separately:

```bash
./dist/datadigitizer \
  --pic-dir /path/to/plot.png \
  --color 255,0,0 \
  --tick-setting "[10,90],[190,90],[10,90],[10,10]" \
  --xmin 0 --xmax 10 --ymin 0 --ymax 100
```

Leave `--color`, `--ticks` / `--tick-setting`, and `--axis-values` blank or pass `null` to use the automatic paths. Outputs are a CSV of digitized data points and an overlapping plot PNG in `--output-dir`, or beside the input image when `--output-dir` is blank.

## GitHub Release Build

The `Build macOS 2.11.mac` workflow builds on the `macos-26` runner and uploads release zips. Pushing tag `v2.11.mac` creates a GitHub Release with the generated artifacts.

## Distribution Notes

These builds are ad-hoc signed for local execution, but they are not Apple Developer ID notarized. On first launch, macOS Gatekeeper may require the user to right-click the app, choose **Open**, and confirm. For wide distribution, add Developer ID signing and notarization secrets to the workflow.
