#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 盛最多水的容器

'''
https://leetcode-cn.com/problems/container-with-most-water/
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
'''

class Solution:
    def maxArea(self, height: 'List[int]') -> int:
        '''
        时间复杂度 : O(n)
        执行用时 : 72 ms, 在Container With Most Water的Python3提交中击败了95.49% 的用户
        内存消耗 : 14.2 MB, 在Container With Most Water的Python3提交中击败了98.69% 的用户
        '''
        area = 0
        l = len(height)
        j = l - 1
        i = 0
        while i < j:
            if height[i] < height[j]:
                a = height[i] * (j - i)
                i += 1
            else:
                a = height[j] * (j - i)
                j -= 1
            if a > area:
                area = a
        return area

    def maxArea2(self, height: 'List[int]') -> int:
        '''
        时间复杂度 : O(n)
        执行用时 : 100 ms, 在Container With Most Water的Python3提交中击败了37.33% 的用户
        内存消耗 : 14.4 MB, 在Container With Most Water的Python3提交中击败了86.28% 的用户
        '''
        area = 0
        l = len(height)
        j = l - 1
        i = 0
        while i < j:
            a = (j - i) * min(height[i], height[j])
            area = max(a, area)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return area

    def maxArea1(self, height: 'List[int]') -> int:
        '''
        时间复杂度 : O(n ** 2)
        暴力解法，超出时间限制
        https://leetcode-cn.com/submissions/detail/18037296/
        '''
        area = 0
        for i in range(len(height)):
            for j in range(1, len(height)):
                k = i + j
                if k < len(height):
                    a = min(height[i], height[k]) * (k - i)
                    area = max(a, area)
        return area

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
        nums = [1,8,6,2,5,4,8,3,7]
        self.assertEqual(func(nums), 49)
        nums = [1]
        self.assertEqual(func(nums), 0)
        nums = [1, 2]
        self.assertEqual(func(nums), 1)
        nums = [1, 2, 3]
        self.assertEqual(func(nums), 2)
        nums = [1, 8, 3, 4]
        self.assertEqual(func(nums), 8)
        nums = [1, 1, 1, 4]
        self.assertEqual(func(nums), 3)


    def test_func(self):
        self.do(s.maxArea2)
        self.do(s.maxArea1)
        self.do(s.maxArea)

if __name__ == "__main__":
    count = 10000
    nums = [1,8,6,2,5,4,8,3,7]
    utils.print_func_run_time(count, s.maxArea1, height = nums)
    utils.print_func_run_time(count, s.maxArea2, height = nums)
    utils.print_func_run_time(count, s.maxArea, height = nums)

    unittest.main()

