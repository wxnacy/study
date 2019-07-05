#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

import unittest

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def do(self, func):
        '''todo'''
        self.assertEqual(1, 1)
        pass

    def test_func(self):
        a = averager()
        next(a)
        self.assertEqual(10.0, a.send(10))
        self.assertEqual(15.0, a.send(20))
        self.assertEqual(20.0, a.send(30))

if __name__ == "__main__":
    unittest.main()

