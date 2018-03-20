#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import unittest

class Test(unittest.TestCase):

    def add(self):
        return 1 + 1

    def divide(self):
        return 0 / 0

    def test_1(self):
        '''test_1 func'''
        self.assertEqual(2, self.add())

    def test_2(self):
        '''test_2 func'''
        self.assertEqual(3, self.add())

    def test_3(self):
        '''test_3 func'''
        self.assertEqual(3, self.divide())

    @unittest.skip("skip this test case")
    def test_4(self):
        '''test_4 func'''
        self.assertEqual(3, self.divide())

if __name__ == "__main__":
    unittest.main(verbosity=2)
    #  unittest.main()
