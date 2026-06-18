#!/usr/bin/env bash
set -euo pipefail

# Build Digitizer.app on macOS and produce a distributable zip.
# Run from a Mac with Homebrew installed:
#   bash build_macos.sh

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

python -m pip install -r requirements.txt
python make_macos_icons.py
bash vendor_tesseract_macos.sh

rm -rf build dist

python -m PyInstaller --clean --noconfirm digitizer_macos.spec

# Ad-hoc sign so Gatekeeper allows a right-click -> Open.
codesign --force --deep --sign - "dist/Digitizer.app" || true

ditto -c -k --sequesterRsrc --keepParent "dist/Digitizer.app" "dist/Digitizer-macos.app.zip"

echo ""
echo "Built: $ROOT/dist/Digitizer.app"
echo "Zip:   $ROOT/dist/Digitizer-macos.app.zip"
