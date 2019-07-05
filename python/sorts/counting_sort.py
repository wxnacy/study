#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import time
import random
import utils

def counting_sort(nums: list, max_num=0):
    if not max_num:
        max_num = max(nums)
    data = {}
    for n in nums:
        if n not in data:
            data[n] = 0
        data[n] += 1
    res = []
    for i in range(max_num):
        if i in data:
            res.extend([i] * data[i])
    return res

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
        for k, v in utils.generate_randoms():
            self.assertEqual(func(k, 100), v)

    def test_func(self):
        self.do(counting_sort)

if __name__ == "__main__":
    unittest.main()
