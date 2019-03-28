#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: for while generator list_comprehension map 对比速度

def loop_for(n):
    res = []
    for i in range(n):
        res.append(abs(i))
    return res

def loop_while(n):
    i = 0
    res = []
    while i < n:
        res.append(abs(i))
        i += 1
    return res

def loop_generator(n):
    res = (abs(i) for i in range(n))
    res =  list(res)
    return res

def loop_list_compre(n):
    res = [abs(i) for i in range(n)]
    return res

def loop_map(n):
    return list(map(abs, range(n)))

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
        n = 10
        flag = (loop_for(n) == loop_while(n) == loop_generator(n) ==
                loop_list_compre(n) == loop_map(n))
        self.assertTrue(flag)

if __name__ == "__main__":
    count = 1000
    n = 1000
    utils.print_func_run_time(count, loop_for, n = n)
    utils.print_func_run_time(count, loop_while, n = n)
    utils.print_func_run_time(count, loop_generator, n = n)
    utils.print_func_run_time(count, loop_list_compre, n = n)
    utils.print_func_run_time(count, loop_map, n = n)
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
