#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import timeit

def print_run_time(count, do_func, *args):
    b = timeit.default_timer()
    for i in range(count):
        do_func(*args)
    print('{}run {} times used: {}s'.format(
        do_func.__name__.ljust(20),
        count, timeit.default_timer() - b))
