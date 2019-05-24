#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 两数之和

'''
难度：简单

地址：[https://leetcode-cn.com/problems/two-sum/](https://leetcode-cn.com/problems/two-sum/)

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
'''

class Solution(object):

    def twoSum(self, nums, target):
        '''
        暴力解法 时间复杂度 O(n^2)
        测试用例第 28 个时超时
        '''
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                k = j + i
                if k < len(nums):
                    if nums[i] + nums[k] == target:
                        return [i, k]


    def twoSum1(self, nums, target):
        '''
        两遍哈希表 时间复杂度 O(n)
        执行用时 : 56 ms, 在Two Sum的Python3提交中击败了89.57% 的用户
        内存消耗 : 14.7 MB, 在Two Sum的Python3提交中击败了7.13% 的用户
        '''
        m = {}
        for i in range(len(nums)):
            m[nums[i]] = i
        for i in range(len(nums)):
            b = target - nums[i]
            if b in m and m[b] != i:
                return [i, m[b]]



    def twoSum2(self, nums, target):
        """
        一遍哈希表 时间复杂度 O(n)
        执行用时 : 44 ms, 在Two Sum的Python3提交中击败了99.33% 的用户
        内存消耗 : 14 MB, 在Two Sum的Python3提交中击败了56.25% 的用户
        """
        m = {}
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b in m:
                return [m[b], i]
            m[a] = i

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
        self.assertEqual(func([2, 7, 11, 15], 9) , [0, 1])
        self.assertEqual(func([2,5,5,11], 10) , [1, 2])
        self.assertEqual(func([0,4,3,0], 0) , [0, 3])
        self.assertEqual(func([-3,4,3,90], 0) , [0, 2])
        self.assertEqual(func([3,2,4], 6) , [1, 2])
        self.assertEqual(func([-1,-2,-3,-4,-5], -8) , [2, 4])
        pass

    def test_func(self):
        self.do(s.twoSum)
        self.do(s.twoSum1)
        self.do(s.twoSum2)

if __name__ == "__main__":
    tm = TestMain()
    import utils
    count = 1000
    utils.print_unittest_do_run_time(count, tm.do, s.twoSum)
    utils.print_unittest_do_run_time(count, tm.do, s.twoSum1)
    utils.print_unittest_do_run_time(count, tm.do, s.twoSum2)
    unittest.main()

#  || .
#  || ----------------------------------------------------------------------
#  || Ran 1 test in 0.000s
#  ||
#  || OK
#  || twoSum               run 1000 times used 0.02609891000611242s
#  || twoSum1              run 1000 times used 0.022648821002803743s
#  || twoSum2              run 1000 times used 0.019425531005254015s
