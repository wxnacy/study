#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 搜索插入位置 简单

'''
https://leetcode-cn.com/problems/search-insert-position/
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0
'''

class Solution:
    def searchInsert1(self, nums: 'List[int]', target: int) -> int:
        '''
        二分查找法
        执行用时 : 44 ms, 在Search Insert Position的Python3提交中击败了98.35% 的用户
        内存消耗 : 13.6 MB, 在Search Insert Position的Python3提交中击败了84.48% 的用户
        '''
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            val = nums[mid]
            if val == target:
                return mid
            elif val > target:
                right = mid - 1
            elif val < target:
                left = mid + 1
        return left

    def searchInsert(self, nums: 'List[int]', target: int) -> int:
        '''
        二分查找法
        执行用时 : 44 ms, 在Search Insert Position的Python3提交中击败了98.35% 的用户
        内存消耗 : 13.6 MB, 在Search Insert Position的Python3提交中击败了84.48% 的用户
        '''
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            val = nums[mid]
            if val == target:
                return mid
            elif val > target:
                right = mid
            elif val < target:
                left = mid + 1
        return left

s = Solution()

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
        self.assertEqual(func([1,3,5,6], 5), 2)
        self.assertEqual(func([1,3,5,6], 2), 1)
        self.assertEqual(func([1,3,5,6], 7), 4)
        self.assertEqual(func([1,3,5,6], 0), 0)
        self.assertEqual(func([1], 1), 0)
        pass

    def test_func(self):
        self.do(s.searchInsert)

if __name__ == "__main__":
    unittest.main()

