# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['ascii_arts.py'],
             pathex=['C:\\Users\\Darshana\\Desktop\\ASCII arts\\bin'],
             binaries=[],
             datas=[('C:\\Users\\Darshana\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\pyfiglet', './pyfiglet')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='ascii_arts',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )