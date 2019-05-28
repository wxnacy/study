#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 只出现一次的数字
'''
难度：简单

知识点：哈希表、位运算

地址：[https://leetcode-cn.com/problems/single-number/](https://leetcode-cn.com/problems/single-number/)

```
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明:

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

    输入: [2,2,1]
    输出: 1
示例 2:

    输入: [4,1,2,1,2]
    输出: 4
```
'''

class Solution:
    def singleNumber(self, nums) -> int:
        '''
        哈希表，严格说不符合题目的要求
        执行用时 : 48 ms, 在Single Number的Python3提交中击败了99.17% 的用户
        内存消耗 : 14.8 MB, 在Single Number的Python3提交中击败了31.34% 的用户
        '''
        m = {}
        for n in nums:
            if n not in m:
                m[n] = 1
            else:
                del m[n]
        for k, v in m.items():
            return k

    def singleNumber1(self, nums) -> int:
        '''
        异或运算
        执行用时 : 52 ms, 在Single Number的Python3提交中击败了95.36% 的用户
        内存消耗 : 14.6 MB, 在Single Number的Python3提交中击败了87.87% 的用户
        '''
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]

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
        self.assertEqual(func([2, 2, 1]), 1)
        self.assertEqual(func([4, 1, 2, 1, 2]), 4)
        pass

    def test_func(self):
        self.do(s.singleNumber)
        self.do(s.singleNumber1)

if __name__ == "__main__":
    unittest.main()
