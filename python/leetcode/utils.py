#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import time

def print_func_run_time(count, func, **kw):
    b = time.clock()
    for i in range(count):
        func(**kw)
    print(func.__name__, 'run {} times used {}s'.format(count, time.clock() -b ))
