#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import unittest
import utils
import quick_sort

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def do(self, func):
        '''todo'''
        for k, v in utils.randoms:
            func(k)
            self.assertEqual(k, v)

    def test_func(self):
        self.do(quick_sort.quick_sort)

if __name__ == "__main__":
    unittest.main()
    print(randoms)
