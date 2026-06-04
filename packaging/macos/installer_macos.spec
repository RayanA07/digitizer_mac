# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path


block_cipher = None
spec_dir = Path(SPECPATH)
root = spec_dir.parents[1]

datas = []

a = Analysis(
    [str(root / "macos_installer.py")],
    pathex=[str(root)],
    binaries=[],
    datas=datas,
    hiddenimports=[],
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
    name="DataDigitizer Installer",
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
    name="DataDigitizer Installer",
)

app = BUNDLE(
    coll,
    name="DataDigitizer Installer.app",
    icon=str(root / "assets" / "digitizer.icns"),
    bundle_identifier="com.aj24by7.datadigitizer.installer",
    info_plist={
        "CFBundleDisplayName": "DataDigitizer Installer",
        "CFBundleShortVersionString": "2.11.mac",
        "CFBundleVersion": "2.11.mac",
        "NSHighResolutionCapable": True,
    },
)
