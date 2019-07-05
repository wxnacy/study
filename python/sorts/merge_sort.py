#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 归并排序

import time
import random
import utils

def merge_sort(nums: list):
    def _merge(left, right):
        res = []
        while left and right:
            res.append(left.pop(0) if left[0] < right[0] else  right.pop(0))
        return res + left + right
    length = len(nums)
    if length < 2:
        return nums
    mid = length // 2
    return _merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))

def merge_sort_fastest(nums: list):
    left, right = [], []
    colls = list(nums)
    while len(colls) > 1:
        min_num, max_num = min(colls), max(colls)
        left.append(min_num)
        right.append(max_num)
        colls.remove(min_num)
        colls.remove(max_num)
    right.reverse()
    return left + colls + right

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
            self.assertEqual(func(k), v)

    def test_func(self):
        self.do(merge_sort)
        self.do(merge_sort_fastest)

if __name__ == "__main__":
    count = 10
    tm = TestMain()
    utils.print_unittest_do_run_time(count, tm.do, merge_sort)
    utils.print_unittest_do_run_time(count, tm.do, merge_sort_fastest)
    unittest.main()
