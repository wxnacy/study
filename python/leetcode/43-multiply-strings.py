#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 字符串相乘

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
执行用时 : 296 ms , 在所有Python3提交中击败了 28.74% 的用户
内存消耗 : 13 MB , 在所有Python3提交中击败了 97.59% 的用户
        '''
        if not num1 or not num2:
            return num1 + num2
        if num1[0] == "0" or num2[0] == "0":
            return "0"
        res = 0
        c1 = 0
        for i1 in range(len(num1) - 1, -1, -1):
            c2 = c1
            for i2 in range(len(num2) - 1, -1, -1):
                n3 = int(num1[i1]) * int(num2[i2]) * ( 10 ** c2)
                res += n3
                c2 += 1
            c1 += 1
        return str(res)

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
        #  self.assertEqual(func("2", "3"), "6")
        self.assertEqual(func("123", "456"), "56088")
        pass

    def test_func(self):
        self.do(s.multiply)

if __name__ == "__main__":
    unittest.main()



