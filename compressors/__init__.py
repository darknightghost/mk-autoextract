#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
      Copyright 2016,王思远 <darknightghost.cn@gmail.com>
      This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
      You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import os
import importlib

def get_compressor_list():
    ret = []
    file_list = os.listdir(os.path.dirname(__file__))

    for f in file_list:
        if f[-3: ] == ".py":
            if f not in ("__init__.py", "Compressor.py"):
                ret.append(os.path.splitext(f)[0])

    return ret

def get_compressor(name):
    return importlib.import_module("compressors.%s"%(name)).Compressor
