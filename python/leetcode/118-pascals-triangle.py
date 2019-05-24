#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 杨辉三角 简单

'''
https://leetcode-cn.com/problems/pascals-triangle/

给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。


在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution:

    def generate(self, numRows: int) -> 'List[List[int]]':
        '''
        执行用时 : 84 ms, 在Pascal's Triangle的Python3提交中击败了10.92% 的用户
        内存消耗 : 13.1 MB, 在Pascal's Triangle的Python3提交中击败了81.20% 的用户
        '''
        res = []
        def make(n):
            rows = [1] * n
            if n < 3:
                return rows
            else:
                for i in range(1, n - 1):
                    rows[i] = res[n - 2][i] + res[n - 2][i - 1]
            return rows
        for i in range(numRows):
            res.append(make(i + 1))
        return res

    def generate1(self, numRows: int) -> 'List[List[int]]':
        '''
        '''
        res = []
        rows = [1]
        for n in range(numRows):
            res.append(rows)
            rows = [sum(o) for o in zip([0] + rows, rows + [0])]
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
        res = [
            [1],
            [1,1],
            [1,2,1],
            [1,3,3,1],
            [1,4,6,4,1]
        ]
        self.assertEqual(func(5), res)
        pass

    def test_func(self):
        self.do(s.generate)
        self.do(s.generate1)

if __name__ == "__main__":
    import utils
    count = 100
    utils.print_func_run_time(count, s.generate, numRows = 100)
    utils.print_func_run_time(count, s.generate1, numRows = 100)
    unittest.main()

