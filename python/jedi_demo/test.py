#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import jedi
import sys
import os

source = '''import datetime;datetime.da'''

script = jedi.Script(source, 1, len(source), '')
#  print(script)
comp = script.completions();
for c in comp: print(c.name, c.full_name, c.complete, c.description, c.module_name,c.module_path)
#  print(comp)
