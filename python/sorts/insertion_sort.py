#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import time
import random
import utils

def insertion_sort(nums: list):
    for i in range(1, len(nums)):
        current = nums[i]
        prefix = i - 1
        while prefix >= 0 and nums[prefix] > current:
            nums[prefix + 1] = nums[prefix]
            prefix -= 1
        nums[prefix + 1] = current

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
        self.do(insertion_sort)

if __name__ == "__main__":
    unittest.main()
