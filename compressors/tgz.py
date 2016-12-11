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

import compressors.Compressor
import tarfile
import os

class Compressor(compressors.Compressor.Compressor):
    def mksfx(self):
        tmp_file = self.output + ".tmp"

        print("Compressing...")
        with tarfile.open(tmp_file, "w:gz") as tar:
            tar.add(self.input_dir, arcname="/")

        tar.close()
        size = os.path.getsize(tmp_file)
        self.__mk_extract_header([], size)

        print("Making sfx file...")
        f = open(self.output, "wb")
        f.write(self.extract_header)

        ftmp = open(tmp_file, "rb")
        
        data = ftmp.read(4096)
        copied = len(data)
        f.write(data)
        print("%d byte(s) copied."%(copied), end = "")

        while len(data) > 0:
            data = ftmp.read(4096)
            copied += len(data)
            f.write(data)
            print("\r%d byte(s) copied."%(copied), end = "")

        print("")
        ftmp.close()
        os.unlink(tmp_file)

        f.close()

        os.chmod(self.output, os.stat(self.output).st_mode | 0o0111)

        return 0

    def translate_args(self, arg_dict):
        return True

    def get_options():
        return []
