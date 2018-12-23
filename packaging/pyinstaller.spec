# -*- mode: python -*-
# coding=utf-8

import os, shutil

# Globals #####################################################################
django_base_dir = os.path.join('..','backend','mowimu_backend')
django_manage_py =  os.path.join(django_base_dir,'manage.py')

# Cleanup #####################################################################
print("Deleting 'dist' directory...")
shutil.rmtree('dist')
os.mkdir("dist")

# Pre-requisites ##############################################################
print("Collecting static files")
os.system("python " + django_manage_py + " collectstatic --noinput")

print("Applying DB migrations")
db_file = os.path.join(django_base_dir, 'db.sqlite3')
db_temp_file = os.path.join(django_base_dir, 'db.sqlite3.tmp')
db_dist_file = os.path.join('dist', 'db.sqlite3')

# Make a backup of the 'db.sqlite3' file in the working tree (if it exists)
try:
    os.remove(db_temp_file)
except FileNotFoundError:
    pass

try:
    os.rename(db_file, db_temp_file)
except FileNotFoundError:
    pass

# Run Django migrations to create a fresh DB file
os.system("python " + django_manage_py + " migrate")

# Copy the fresh DB to the 'dist' directory
os.rename(db_file, db_dist_file)

# Restore the backup of the original 'db.sqlite3' file in the working tree (if it existed)
try:
    os.rename(db_temp_file, db_file)
except FileNotFoundError:
    pass

# PyInstaller #################################################################
block_cipher = None
entry_point =  django_manage_py
binary_name = 'mowimu'

a = Analysis([entry_point],
             pathex=[os.path.join('..','backend','mowimu_backend'),
                     os.path.abspath(os.path.join('..', 'backend'))],
             binaries=[],
             datas=[(os.path.join('..','backend','mowimu_backend','static'),'static')],
             hiddenimports=[],
             hookspath=[os.path.join('.', 'pyinstaller_hooks')],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

# append the 'static' dir
# a.datas += (os.path.join('..','backend','mowimu_backend','static'),'static')

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=binary_name,
          debug=False,
          strip=False,
          upx=True,
          console=True )
