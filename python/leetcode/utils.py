#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import timeit

def print_func_run_time(count, func, **kw):
    b = timeit.default_timer()
    for i in range(count):
        func(**kw)
    print(func.__name__, 'run {} times used {}s'.format(count,
        timeit.default_timer() -b ))

if __name__ == "__main__":
    pass
