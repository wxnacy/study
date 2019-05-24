#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 杨辉三角 II 简单

'''
https://leetcode-cn.com/problems/pascals-triangle-ii/

给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？
'''

class Solution:
    def getRow(self, rowIndex: int) -> 'List[int]':
        pass

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
        res = [1,4,6,4,1]
        self.assertEqual(func(4), res)
        pass

    def test_func(self):
        self.do(s.generate)
        #  self.do(s.generate1)

if __name__ == "__main__":
    import utils
    count = 100
    utils.print_func_run_time(count, s.generate, numRows = 100)
    #  utils.print_func_run_time(count, s.generate1, numRows = 100)
    unittest.main()

