#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import timeit
import utils

def min_if(a, b):
    if a < b:
        return a
    return b

def min_ifelse(a, b):
    return a if a < b else b

if __name__ == "__main__":
    count = 5000
    utils.print_run_time(count, min_if, 1, 2)
    utils.print_run_time(count, min_if, 2, 1)
    utils.print_run_time(count, min_ifelse, 3, 4)
    utils.print_run_time(count, min_ifelse, 4, 3)
    utils.print_run_time(count, min, 5, 6)
    utils.print_run_time(count, min, 6, 5)
