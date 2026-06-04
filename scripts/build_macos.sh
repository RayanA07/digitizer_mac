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
python -m PyInstaller --clean --noconfirm packaging/macos/installer_macos.spec

codesign --force --deep --sign - "dist/Digitizer.app" || true
codesign --force --deep --sign - "dist/AccuracyTester.app" || true
codesign --force --sign - "dist/datadigitizer" || true
codesign --force --deep --sign - "dist/DataDigitizer Installer.app" || true

mkdir -p release
cp "MACOS_INSTALL_MANUAL.txt" "release/MACOS_INSTALL_MANUAL.txt"

ditto -c -k --sequesterRsrc --keepParent "dist/Digitizer.app" "release/Digitizer-2.11.mac.app.zip"
ditto -c -k --sequesterRsrc --keepParent "dist/AccuracyTester.app" "release/AccuracyTester-2.11.mac.app.zip"
ditto -c -k --keepParent "dist/datadigitizer" "release/datadigitizer-cli-2.11.mac.zip"
ditto -c -k --sequesterRsrc --keepParent "dist/DataDigitizer Installer.app" "release/DataDigitizer-2.11.mac-Installer.app.zip"

rm -rf "release/package-root"
mkdir -p "release/package-root/DataDigitizer-2.11.mac"
cp -R "dist/DataDigitizer Installer.app" "release/package-root/DataDigitizer-2.11.mac/"
cp -R "dist/Digitizer.app" "release/package-root/DataDigitizer-2.11.mac/"
cp -R "dist/AccuracyTester.app" "release/package-root/DataDigitizer-2.11.mac/"
cp "dist/datadigitizer" "release/package-root/DataDigitizer-2.11.mac/"
cp "README.md" "RELEASE_NOTES.md" "MACOS_INSTALL_MANUAL.txt" "release/package-root/DataDigitizer-2.11.mac/"
ditto -c -k --sequesterRsrc --keepParent \
  "release/package-root/DataDigitizer-2.11.mac" \
  "release/DataDigitizer-2.11.mac-macOS.zip"
rm -rf "release/package-root"

echo "Release artifacts:"
ls -lh release
