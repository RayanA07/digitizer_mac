# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

from PyInstaller.utils.hooks import collect_data_files, collect_submodules


block_cipher = None
spec_dir = Path(SPECPATH)
root = spec_dir.parents[1]

datas = [(str(root / "version.json"), ".")]
datas += collect_data_files("matplotlib")
datas += collect_data_files("tkinterdnd2")
hiddenimports = collect_submodules("tkinterdnd2")

a = Analysis(
    [str(root / "accuracytester_desktop.py")],
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
    name="AccuracyTester",
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
    name="AccuracyTester",
)

app = BUNDLE(
    coll,
    name="AccuracyTester.app",
    icon=str(root / "assets" / "accuracytester.icns"),
    bundle_identifier="com.aj24by7.datadigitizer.accuracytester",
    info_plist={
        "CFBundleDisplayName": "AccuracyTester",
        "CFBundleShortVersionString": "2.11.mac",
        "CFBundleVersion": "2.11.mac",
        "NSHighResolutionCapable": True,
    },
)
