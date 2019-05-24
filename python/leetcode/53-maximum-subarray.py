#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 最大子序和 为完成动态规划算法

'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''

from constants import NUMS_FOR53

class Solution:

    def maxSubArray1(self, nums) -> int:
        '''
        暴力解法，时间超限，详见
        https://leetcode-cn.com/submissions/detail/18022319/
        '''
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        max_sum = -2 ** 23
        sums = []
        for i in range(len(nums)):
            sums.append(nums[i])
            if nums[i] > max_sum:
                max_sum = nums[i]
            for j in range(len(nums)):
                k = i + j + 1
                if k >= len(nums):
                    break
                s = sums[-1] + nums[k]
                sums.append(s)
                if s > max_sum:
                    max_sum = s

        return max_sum

    def maxSubArray2(self, nums) -> int:
        '''
        时间复杂度 : O(n)
        执行用时 : 64 ms, 在Maximum Subarray的Python3提交中击败了72.70% 的用户
        内存消耗 : 13.4 MB, 在Maximum Subarray的Python3提交中击败了96.67% 的用户
        '''
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        max_index = 0
        max_val = -2 ** 23

        s = max_val
        max_s = s
        b = -1
        i = 0
        l = len(nums)
        for i in range(l):
            if nums[i] > max_val:
                max_val = nums[i]
                max_index = i
            if b == -1 and nums[i] > 0 and i < l - 1:
                bv = nums[i] + nums[i + 1]
                if bv > 0:
                    b = i
                    s = nums[i]
                    if s > max_s:
                        max_s = s
            else:
                s+=nums[i]
                if s <=0:
                    b = -1
                if s > max_s:
                    max_s = s
        return max_s if max_s > max_val else max_val

    def maxSubArray3(self, nums) -> int:
        '''
        时间复杂度 : O(n)
        执行用时 : 64 ms, 在Maximum Subarray的Python3提交中击败了72.70% 的用户
        内存消耗 : 13.4 MB, 在Maximum Subarray的Python3提交中击败了96.67% 的用户
        '''
        if not nums:
            return 0
        s = 0
        max_sum = nums[0]
        for n in nums:
            s += n
            if s > max_sum:
                max_sum = s
            if s < 0:
                s = 0
        return max_sum

    def maxSubArray4(self, nums) -> int:
        '''
        时间复杂度 : O(n)
        执行用时 : 64 ms, 在Maximum Subarray的Python3提交中击败了72.70% 的用户
        内存消耗 : 13.4 MB, 在Maximum Subarray的Python3提交中击败了96.67% 的用户
        '''
        if not nums:
            return 0

        s = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            if nums[i] > s:
                s = nums[i]
        return s


import unittest
import utils

s = Solution()

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def do(self, func):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(func(nums), 6)
        nums = [-2, 1]
        self.assertEqual(func(nums), 1)
        nums = [-2, -1]
        self.assertEqual(func(nums), -1)
        nums = [1, 2]
        self.assertEqual(func(nums), 3)
        nums = [1, 1, -2]
        self.assertEqual(func(nums), 2)
        nums = [3,1,-3,-3,2,-1]
        self.assertEqual(func(nums), 4)
        nums = [8,-19,5,-4,20]
        self.assertEqual(func(nums), 21)
        nums = [2,0,-3,2,1,0,1,-2]
        self.assertEqual(func(nums), 4)
        #  for nums in TEST_LISTS:
            #  self.assertEqual(s.maxSubArray2(nums), func(nums))

    def test_func(self):
        s = Solution()
        self.do(s.maxSubArray4)
        self.do(s.maxSubArray3)
        self.do(s.maxSubArray2)
        self.do(s.maxSubArray1)

if __name__ == "__main__":
    count = 100
    tm = TestMain()
    utils.print_func_run_time(count, s.maxSubArray2, nums = NUMS_FOR53)
    utils.print_func_run_time(count, s.maxSubArray3, nums = NUMS_FOR53)
    utils.print_func_run_time(count, s.maxSubArray4, nums = NUMS_FOR53)
    #  utils.print_func_run_time1(count, tm.do, s.maxSubArray3)
    unittest.main()


