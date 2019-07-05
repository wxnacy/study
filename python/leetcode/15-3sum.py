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
    def twoSum(self, nums, target):
        m = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in m:
                return [m[n], i]
            m[nums[i]] = i
        return [0, 0]

    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        '''
执行用时 : 1208 ms, 在3Sum的Python3提交中击败了58.01% 的用户
内存消耗 : 16.6 MB, 在3Sum的Python3提交中击败了93.52% 的用户
        '''
        res = []
        if not nums:
            return res
        nums.sort()
        if ( nums[0] > 0 and nums[-1] > 0 ) or ( nums[0] < 0 and nums[-1] < 0):
            return res
        length = len(nums)
        last_begin = nums[0]
        for i in range(length - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == last_begin:
                continue
            last_begin = nums[i]
            left = i + 1
            right = length - 1
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                if _sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                if _sum <= 0:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and  nums[right + 1] == nums[right]:
                        right -=1
        return res

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
        res = [ [-1, -1, 2],[-1, 0, 1]  ]
        self.assertEqual(func(nums), res)
        self.assertEqual(func([]), [])
        self.assertEqual(func([0, 0, 0, 0]), [[0, 0, 0]])

    def test_func(self):
        self.do(s.threeSum)

if __name__ == "__main__":
    unittest.main()
