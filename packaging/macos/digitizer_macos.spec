# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path


block_cipher = None
spec_dir = Path(SPECPATH)
root = spec_dir.parents[1]

datas = [(str(root / "version.json"), ".")]
vendor_tesseract = root / "vendor" / "tesseract"
if vendor_tesseract.exists() and any(path.is_file() for path in vendor_tesseract.rglob("*")):
    datas.append((str(vendor_tesseract), "vendor/tesseract"))

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
    icon=str(root / "assets" / "digitizer.icns"),
    bundle_identifier="com.aj24by7.datadigitizer.digitizer",
    info_plist={
        "CFBundleDisplayName": "Digitizer",
        "CFBundleShortVersionString": "2.11.mac",
        "CFBundleVersion": "2.11.mac",
        "NSHighResolutionCapable": True,
    },
)
