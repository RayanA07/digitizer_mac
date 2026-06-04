# 2.11.mac

macOS Tahoe release package for Data Digitizer 2.11.

Included:

- `DataDigitizer Installer.app` windowed installer with progress bar
- installer copies apps to `~/Applications/Data Digitizer`
- installer creates Desktop launchers for Digitizer, AccuracyTester, and CLI help
- `Digitizer.app` desktop app
- `AccuracyTester.app` desktop app
- `datadigitizer` CLI executable
- one-line `digitizer_cli(...)` CLI syntax matching the Windows 2.11 wrapper
- CLI inputs for `pic_dir`, RGB color, tick setting, axis bounds, and output directory
- CLI outputs for digitized CSV data and an overlapping plot PNG
- explicit `interactive` CLI fallback command
- bundled Tesseract OCR runtime for digitizer OCR features
- GitHub Actions macOS build and release workflow

Build target:

- macOS Tahoe via GitHub Actions `macos-26`
- Python 3.11
- PyInstaller app bundles plus a CLI executable

Note:

- Builds are ad-hoc signed but not Apple Developer ID notarized. Gatekeeper may require right-click / Control-click -> Open, or quarantine removal with `xattr`.
