# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\Markus\\Documents\\GITHUB\\Software_Programmierung\\Schulsachen\\3BWHII\\OOP\\GUI_textadventure\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\Markus\\Documents\\GITHUB\\Software_Programmierung\\Schulsachen\\3BWHII\\OOP\\GUI_textadventure\\modules', 'modules')],
    hiddenimports=['customtkinter'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
