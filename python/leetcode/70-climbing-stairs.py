#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 爬楼梯 简单

'''
https://leetcode-cn.com/problems/climbing-stairs/
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        n = 38 超时
        '''
        def climb(n: int):
            if n <= 3:
                return n
            else:
                return climb(n-1) + climb(n - 2)
        return climb(n)

    steps = []
    def climbStairs1(self, n: int) -> int:
        '''
        执行用时 : 76 ms, 在Climbing Stairs的Python3提交中击败了17.58% 的用户
        内存消耗 : 13 MB, 在Climbing Stairs的Python3提交中击败了97.24% 的用户
        '''
        if len(self.steps) < n:
            for i in range(n):
                if i <= 2:
                    if len(self.steps) <= i:
                        self.steps.append(i+1)
                else:
                    if len(self.steps) <= i:
                        self.steps.append(self.steps[i - 1] + self.steps[i - 2])
        return self.steps[n-1]

    def climbStairs2(self, n: int) -> int:
        '''
        执行用时 : 52 ms, 在Climbing Stairs的Python3提交中击败了76.91% 的用户
        内存消耗 : 13.1 MB, 在Climbing Stairs的Python3提交中击败了82.25% 的用户
        '''
        if n <= 3:
            return n
        a, b = 2, 3
        total = 0
        for i in range(3, n):
            total = a + b
            a, b = b, total
        return total

s = Solution()

import unittest
import utils

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def do(self, func):
        self.assertEqual(func(1), 1)
        self.assertEqual(func(2), 2)
        self.assertEqual(func(3), 3)
        self.assertEqual(func(4), 5)

    def test_func(self):
        self.do(s.climbStairs)
        self.do(s.climbStairs1)
        self.do(s.climbStairs2)

if __name__ == "__main__":
    count = 1
    #  utils.print_func_run_time(count, s.climbStairs, n = 38)
    utils.print_func_run_time(count, s.climbStairs1, n = 10000)
    utils.print_func_run_time(count, s.climbStairs2, n = 10000)

    unittest.main()
