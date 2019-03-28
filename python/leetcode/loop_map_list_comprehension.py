#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: for while generator list_comprehension map 对比速度


def make_data(n):
    def _make(i):
        item = dict(id = i)
        return item
    return list(map(_make, range(n)))


def fmt(o):
    if o['id'] < 50:
        o['name'] = "<50"
    else:
        o['name'] = ">=50"
    return o

def loop_list_compre(items):
    res = [fmt(i) for i in items]
    return res

def loop_map(items):
    return list(map(fmt, items))

import utils
import unittest

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def test_func(self):
        items = make_data(10)
        flag = (loop_list_compre(items) == loop_map(items))
        self.assertTrue(flag)

if __name__ == "__main__":
    count = 1000
    n = 1000
    items = make_data(1000)
    utils.print_func_run_time(count, loop_list_compre, items = items)
    utils.print_func_run_time(count, loop_map, items = items)
    unittest.main()

# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK
# loop_for             run 1000 times used 0.14018906400087872s
# loop_while           run 1000 times used 0.21399457900042762s
# loop_generator       run 1000 times used 0.12857274799898732s
# loop_list_compre     run 1000 times used 0.08585307099929196s
# loop_map             run 1000 times used 0.043123570998432115s
