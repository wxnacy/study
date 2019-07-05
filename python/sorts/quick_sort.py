#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import time
import random
import utils

def quick_sort(nums: list):
    '''
    每次都以最左边的索引当做划分点
    '''
    def partition(nums, left, right):
        t = nums[left]                      # 找出想要作为分割位的中间值
        x = left                            # 将左侧坐标重新初始化
        y = right                           # 将右侧坐标重新初始化
        while x < y:                        # 完成一次左右坐标相遇
            while x < y and nums[y] >= t:   # 先从右侧查找一次小于中间值的数字
                y -= 1
            nums[x] = nums[y]               # 将找到的数字赋值到左坐标的位置
            while x < y and nums[x] <= t:   # 先从左侧查找一次大于中间值的数字
                x += 1
            nums[y] = nums[x]               # 将找到的数字赋值到空出的右侧坐标位

        nums[x] = t                         # 将中间值赋值到最后空出位置上
        return x                            # 返回此次最终的中间位置

    def _sort(nums, left, right):
        if left < right:
            index = partition(nums, left, right) # 将数组做第一次分治
            _sort(nums, left, index - 1)         # 将左侧数据做下一步分治
            _sort(nums, index + 1, right)        # 将右侧数据做下一步分治

    _sort(nums, 0, len(nums) - 1)

def quick_sort_3partition(nums: list):

    def _sort(nums, left, right):
        if right <= left:
            return
        a = i = left
        b = right
        pivot = nums[left]
        while i <= b:
            if nums[i] < pivot:
                nums[i], nums[a] = nums[a], nums[i]
                a += 1
                i += 1
            elif nums[i] > pivot:
                nums[i], nums[b] = nums[b], nums[i]
                b -= 1
            else:
                i += 1

        _sort(nums, left, a - 1)
        _sort(nums, b + 1, right)

    _sort(nums, 0, len(nums) - 1)



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
        self.do(quick_sort)
        self.do(quick_sort_3partition)

if __name__ == "__main__":
    unittest.main()
