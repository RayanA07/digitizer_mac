#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

python -m pip install -r requirements-macos.txt
python scripts/make_macos_icons.py
bash scripts/vendor_tesseract_macos.sh

rm -rf build dist release

python -m PyInstaller --clean --noconfirm packaging/macos/digitizer_macos.spec
python -m PyInstaller --clean --noconfirm packaging/macos/accuracytester_macos.spec
python -m PyInstaller --clean --noconfirm packaging/macos/datadigitizer_cli_macos.spec

codesign --force --deep --sign - "dist/Digitizer.app" || true
codesign --force --deep --sign - "dist/AccuracyTester.app" || true
codesign --force --sign - "dist/datadigitizer" || true

mkdir -p release

ditto -c -k --sequesterRsrc --keepParent "dist/Digitizer.app" "release/Digitizer-2.11.mac.app.zip"
ditto -c -k --sequesterRsrc --keepParent "dist/AccuracyTester.app" "release/AccuracyTester-2.11.mac.app.zip"
ditto -c -k --keepParent "dist/datadigitizer" "release/datadigitizer-cli-2.11.mac.zip"
ditto -c -k --sequesterRsrc --keepParent \
  "dist/Digitizer.app" \
  "dist/AccuracyTester.app" \
  "dist/datadigitizer" \
  "README.md" \
  "RELEASE_NOTES.md" \
  "release/DataDigitizer-2.11.mac-macOS.zip"

echo "Release artifacts:"
ls -lh release
