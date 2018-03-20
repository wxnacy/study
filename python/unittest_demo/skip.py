#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import unittest

class Test(unittest.TestCase):

    def add(self):
        return 1 + 1

    @unittest.skip("skip test_1 case")
    def test_1(self):
        '''test_1'''
        self.assertEqual(2, self.add())

    def test_2(self):
        '''test_2'''
        self.skipTest('skip test_2 case')
        self.assertEqual(3, self.add())

    @unittest.skipIf(1 == 1, 'skip test_3 case')
    def test_3(self):
        self.assertEqual(3, self.add())

    @unittest.skipUnless(1 != 1, 'skip test_4 case')
    def test_4(self):
        self.assertEqual(3, self.add())

if __name__ == "__main__":
    unittest.main()
