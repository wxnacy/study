#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 希尔排序

import time
import random
import utils

def shell_sort(nums: list):
    gap = 1
    while gap < len(nums) // 3:
        gap = gap * 3 + 1

    while gap > 0:
        for i in range(gap, len(nums)):
            tmp = nums[i]
            j = i - gap
            while j >= 0 and nums[j] > nums[i]:
                nums[j + gap] = nums[j]
                i -= 1
            nums[j + gap] = tmp
        gap = gap // 3


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
        self.do(shell_sort)

if __name__ == "__main__":
    unittest.main()
