#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import time
import random
import utils

def radix_sort(nums: list):
    mod = 10
    div = 1
    max_num = max(nums)
    while div < max_num:

        buckets = [[] for _ in range(10)]
        for n in nums:
            i = n % mod // div
            buckets[i].append(n)

        c = 0
        for b in buckets:
            for bn in b:
                nums[c] = bn
                c += 1

        div *= 10
        mod *= 10


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
            func(k)
            self.assertEqual(k, v)

    def test_func(self):
        self.do(radix_sort)

if __name__ == "__main__":
    unittest.main()
