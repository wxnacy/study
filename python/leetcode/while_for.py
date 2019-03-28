#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: while 对比 for 速度


def loop_for(n):
    res = []
    for i in range(n):
        res.append(n)
    return res

def loop_while(n):
    i = 0
    res = []
    while i < n:
        res.append(i)
    return res

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
        n = 100
        self.assertEqual(loop_for(n), loop_while(n))

if __name__ == "__main__":
    count = 1000
    n = 1000
    utils.print_func_run_time(count, loop_for, n = n)
    utils.print_func_run_time(count, loop_while, n = n)
    unittest.main()

