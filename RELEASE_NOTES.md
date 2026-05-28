# 2.11.mac

Initial macOS Tahoe release package for Data Digitizer 2.11.

Included:

- `Digitizer.app` desktop app
- `AccuracyTester.app` desktop app
- `datadigitizer` CLI executable
- interactive CLI wizard
- bundled Tesseract OCR runtime for digitizer OCR features
- GitHub Actions macOS build and release workflow

Build target:

- macOS Tahoe via GitHub Actions `macos-26`
- Python 3.11
- PyInstaller one-folder app bundles plus a one-file CLI executable
