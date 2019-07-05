#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import time
import random
import utils

def selection_sort(nums: list):
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]

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
        self.do(selection_sort)

if __name__ == "__main__":
    unittest.main()
