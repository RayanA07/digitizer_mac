# 2.11.mac

Initial macOS Tahoe release package for Data Digitizer 2.11.

Included:

- `Digitizer.app` desktop app
- `AccuracyTester.app` desktop app
- `datadigitizer` CLI executable
- interactive CLI wizard
- CLI-only `datadigitizer` launcher that opens the input menu when run with no arguments
- one-line CLI inputs for `pic_dir`, RGB color, tick setting, axis bounds, and output directory
- CLI outputs for digitized CSV data and an overlapping plot PNG
- bundled Tesseract OCR runtime for digitizer OCR features
- GitHub Actions macOS build and release workflow

Build target:

- macOS Tahoe via GitHub Actions `macos-26`
- Python 3.11
- PyInstaller one-folder app bundles plus a one-file CLI executable
