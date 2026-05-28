#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENDOR_DIR="$ROOT/vendor/tesseract"
TESSDATA_DIR="$VENDOR_DIR/tessdata"

if ! command -v brew >/dev/null 2>&1; then
  echo "Homebrew is required to vendor Tesseract on macOS." >&2
  exit 1
fi

if ! command -v tesseract >/dev/null 2>&1; then
  brew install tesseract
fi

if ! command -v dylibbundler >/dev/null 2>&1; then
  brew install dylibbundler
fi

rm -rf "$VENDOR_DIR"
mkdir -p "$TESSDATA_DIR"

TESSERACT_BIN="$(command -v tesseract)"
cp "$TESSERACT_BIN" "$VENDOR_DIR/tesseract"
chmod +x "$VENDOR_DIR/tesseract"

BREW_TESS_PREFIX="$(brew --prefix tesseract)"
if [[ -f "$BREW_TESS_PREFIX/share/tessdata/eng.traineddata" ]]; then
  cp "$BREW_TESS_PREFIX/share/tessdata/eng.traineddata" "$TESSDATA_DIR/"
fi
if [[ -f "$BREW_TESS_PREFIX/share/tessdata/osd.traineddata" ]]; then
  cp "$BREW_TESS_PREFIX/share/tessdata/osd.traineddata" "$TESSDATA_DIR/"
fi

if [[ ! -f "$TESSDATA_DIR/eng.traineddata" ]]; then
  echo "Missing eng.traineddata after Tesseract install." >&2
  exit 1
fi

dylibbundler \
  -od \
  -b \
  -x "$VENDOR_DIR/tesseract" \
  -d "$VENDOR_DIR/lib" \
  -p "@executable_path/lib"

echo "Vendored Tesseract runtime at $VENDOR_DIR"
