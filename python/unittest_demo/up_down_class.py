#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import unittest

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('begin setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('begin tearDownClass')

    def add(self):
        return 1 + 1


    def test_1(self):
        self.assertEqual(2, self.add())
        print('run test_1')

    def test_2(self):
        self.assertEqual(2, self.add())
        print('run test_2')



if __name__ == "__main__":
    unittest.main()
