#!/usr/bin/env bash
set -euo pipefail

# Build AccuracyTester.app on macOS and produce a distributable zip.
# No Tesseract needed for this tool.
# Run from a Mac:
#   bash build_macos.sh

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

python -m pip install -r requirements.txt
python make_macos_icons.py

rm -rf build dist

python -m PyInstaller --clean --noconfirm accuracytester_macos.spec

# Ad-hoc sign so Gatekeeper allows a right-click -> Open.
codesign --force --deep --sign - "dist/AccuracyTester.app" || true

ditto -c -k --sequesterRsrc --keepParent "dist/AccuracyTester.app" "dist/AccuracyTester-macos.app.zip"

echo ""
echo "Built: $ROOT/dist/AccuracyTester.app"
echo "Zip:   $ROOT/dist/AccuracyTester-macos.app.zip"
