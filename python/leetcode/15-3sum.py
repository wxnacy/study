#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 三数之和

'''
https://leetcode-cn.com/problems/3sum/
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        res = []
        for n in nums:


        pass

import unittest

s = Solution()

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def do(self, func):
        nums = [-1, 0, 1, 2, -1, -4]
        res = [ [-1, 0, 1], [-1, -1, 2] ]
        self.assertEqual(nums, res)
        nums = [-1, 0, 1]
        res = [ [-1, 0, 1]]
        self.assertEqual(nums, res)
        nums = [-1, 0]
        res = [[]]
        self.assertEqual(nums, res)
        nums = [-1, 0, 1, -1, 0, 1]
        res = [ [-1, 0, 1]]
        self.assertEqual(nums, res)

    def test_func(self):
        self.do(s.threeSum)

if __name__ == "__main__":
    unittest.main()
