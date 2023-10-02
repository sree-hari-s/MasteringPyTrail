# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['/home/nnisarggada/GitRepos/NyChess/main.py'],
    pathex=[],
    binaries=[],
    datas=[('/home/nnisarggada/GitRepos/NyChess/bB.png', '.'), ('/home/nnisarggada/GitRepos/NyChess/bK.png', '.'), ('/home/nnisarggada/GitRepos/NyChess/bN.png', '.'), ('/home/nnisarggada/GitRepos/NyChess/bp.png', '.'), ('/home/nnisarggada/GitRepos/NyChess/bQ.png', '.'), ('/home/nnisarggada/GitRepos/NyChess/bR.png', '.'), ('/home/nnisarggada/GitRepos/NyChess/capture.wav', '.'), ('/home/nnisarggada/GitRepos/NyChess/ChessBrain.py', '.'), ('/home/nnisarggada/GitRepos/NyChess/ChessEngine.py', '.'), ('/home/nnisarggada/GitRepos/NyChess/move.wav', '.'), ('/home/nnisarggada/GitRepos/NyChess/wB.png', '.'), ('/home/nnisarggada/GitRepos/NyChess/wK.png', '.'), ('/home/nnisarggada/GitRepos/NyChess/wN.png', '.'), ('/home/nnisarggada/GitRepos/NyChess/wp.png', '.'), ('/home/nnisarggada/GitRepos/NyChess/wQ.png', '.'), ('/home/nnisarggada/GitRepos/NyChess/wR.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='NyChess (Linux)',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=True,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['/home/nnisarggada/GitRepos/NyChess/Logo.ico'],
)
