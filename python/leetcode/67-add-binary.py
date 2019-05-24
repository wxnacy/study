#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 二进制求和 简单

'''
https://leetcode-cn.com/problems/add-binary/
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        执行用时 : 56 ms, 在Add Binary的Python3提交中击败了85.97% 的用户
        内存消耗 : 13 MB, 在Add Binary的Python3提交中击败了91.20% 的用户
        '''
        c = 0
        if len(b) > len(a):
            a, b = b, a
        res = ''
        for i in range(len(a)):
            bx = int(b[-1 - i]) if -1 - i >= -len(b) else 0
            d = int(a[-1 - i]) + bx + c
            if d < 2:
                res = str(d) + res
                c = 0
                if -1 - i == -len(b):
                    return a[0:-1-i] + res
            else:
                c = 1
                res = str(d - 2) + res
                if -1 - i == -len(a):
                    res = "1" + res
        return res

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
        self.assertEqual(func("11", "1"), "100")
        self.assertEqual(func("1", "1"), "10")
        self.assertEqual(func("10", "1"), "11")
        self.assertEqual(func("1010", "1011"), "10101")
        pass

    def test_func(self):
        self.do(s.addBinary)

if __name__ == "__main__":
    unittest.main()
