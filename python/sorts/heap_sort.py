#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 堆排序

import time
import random
import utils

def heap_sort(nums: list):
    '''
    每次都以最左边的索引当做划分点
    '''
    length = len(nums)

    def heapify(nums, i, heap_len):
        k = i
        left = i * 2 + 1
        right = i * 2 + 2

        if left < heap_len and nums[left] > nums[k]:
            k = left
        if right < heap_len and nums[right] > nums[k]:
            k = right
        if k != i:
            nums[i], nums[k] = nums[k], nums[i]
            heapify(nums, k, heap_len)

    for i in range((length >> 1) - 1, -1, -1):
        heapify(nums, i, length)

    for i in range(length - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, 0, i)

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
        for k, v in utils.randoms:
            func(k)
            self.assertEqual(k, v)

    def test_func(self):
        self.do(heap_sort)

if __name__ == "__main__":
    unittest.main()
