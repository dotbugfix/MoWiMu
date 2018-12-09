#!/usr/bin/env python
import os
import sys

# Explicit imports for PyInstaller
import mowimu_inventory

if __name__ == '__main__':
    if getattr(sys, 'frozen', False) :
        print("PyInstaller Path: ", sys._MEIPASS)
        print("PyInstaller Executable: ", sys.executable)
        from mowimu_backend import settings
        print("Django BASE_DIR: ", settings.BASE_DIR)
        print("PyInstaller dir: ", settings.pyinstaller_exe_dir)

    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mowimu_backend.settings')
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
