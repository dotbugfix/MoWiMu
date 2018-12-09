#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules
hiddenimports = collect_submodules('mowimu_inventory')
hiddenimports += collect_submodules('mowimu_inventory.migrations')