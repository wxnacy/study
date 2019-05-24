#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: x 的平方根 简单

'''
https://leetcode-cn.com/problems/sqrtx/
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
'''

class Solution:

    def mySqrt1(self, x: int) -> int:
        '''
        执行用时 : 108 ms, 在Sqrt(x)的Python3提交中击败了25.50% 的用户
        内存消耗 : 13.2 MB, 在Sqrt(x)的Python3提交中击败了60.51% 的用户
        '''
        if 0 < x <= 3:
            return 1
        y = x // 2
        i = 0
        j = x
        while i < j and y > i:
            if y ** 2 == x:
                return y
            elif y ** 2 < x:
                i = y
            else:
                j = y
            y = (j - i) //2 + i
        return i

    def mySqrt(self, x: int) -> int:
        '''
执行用时 : 52 ms, 在Sqrt(x)的Python3提交中击败了98.44% 的用户
内存消耗 : 13.1 MB, 在Sqrt(x)的Python3提交中击败了85.12% 的用户
        '''
        return int(x ** 0.5)


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
        self.assertEqual(func(4), 2)
        self.assertEqual(func(8), 2)
        self.assertEqual(func(6), 2)
        self.assertEqual(func(7), 2)
        pass

    def test_func(self):
        self.do(s.mySqrt)

if __name__ == "__main__":
    unittest.main()
