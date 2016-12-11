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
import math

class Compressor:
    def __init__(self, input_dir, extract_dir, install_script, output):
        self.input_dir = input_dir
        self.output = output
        
        #Load template file
        template_file_path = os.path.abspath(
            "%s%s%s.template"%(os.path.dirname(__file__),
                os.path.sep,
                self.__class__.__name__))

        f = open(template_file_path, "r")
        lines = f.readlines()
        size = f.tell()
        f.close()

        extract_script = []

        #First line
        extract_script.append(lines[1])

        #Write args
        extract_dir_line = "extract_dir=\"%s\"\n"%(extract_dir)
        install_script_line = "install_script=\"%s\""%(install_script)
        size_line = "size="

        size += len(extract_dir_line.encode('utf-8')) \
                + len(install_script_line.encode('utf-8')) \
                + len(size_line.encode('utf-8'))
        size += 20
        size = math.ceil(size / 8) * 8
        size_line += str(size) + "\n"

        extract_script.append(extract_dir_line)
        extract_script.append(install_script_line)
        extract_script.append(size_line)

        #Read extract script
        for i in range(1, len(lines)):
            extract_script.append(lines(i))

        #Encode extract head
        self.extract_head = b''
        for l in extract_script:
            self.extract_head += l.encode('utf-8')

        if len(self.extract_head) < size:
            self.extract_head += b'\x00' * size.len(self.extract_head)
            

    def mksfx(self):
        raise NotImplementedError()

    def translate_args(self, arg_dict):
        raise NotImplementedError()

    def get_options():
        raise NotImplementedError()
