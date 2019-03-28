#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import timeit

def print_func_run_time(count, func, **kw):
    b = timeit.default_timer()
    for i in range(count):
        func(**kw)
    print('{} run {} times used {}s'.format(
        func.__name__.ljust(20),
        count,
        timeit.default_timer() -b ))

if __name__ == "__main__":
    pass
