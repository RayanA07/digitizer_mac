# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path


block_cipher = None
root = Path(SPECPATH)

datas = [(str(root / "version.json"), ".")]

# Tesseract OCR runtime bundled from Digitizer/vendor/tesseract (self-contained OCR).
vendor_tesseract = root / "vendor" / "tesseract"
if vendor_tesseract.exists() and any(path.is_file() for path in vendor_tesseract.rglob("*")):
    datas.append((str(vendor_tesseract), "vendor/tesseract"))

# Icon is optional: if assets/digitizer.icns is missing, build without one.
icon_path = root / "assets" / "digitizer.icns"
icon = str(icon_path) if icon_path.is_file() else None

hiddenimports = [
    "openpyxl",
    "pytesseract",
    "PIL.Image",
    "PIL.ImageEnhance",
    "PIL.ImageFilter",
    "PIL.ImageOps",
]

a = Analysis(
    [str(root / "digitizer_desktop.py")],
    pathex=[str(root)],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="Digitizer",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="Digitizer",
)

app = BUNDLE(
    coll,
    name="Digitizer.app",
    icon=icon,
    bundle_identifier="com.rayana07.datadigitizer.digitizer",
    info_plist={
        "CFBundleDisplayName": "Digitizer",
        "CFBundleShortVersionString": "2.12",
        "CFBundleVersion": "2.12",
        "NSHighResolutionCapable": True,
    },
)
