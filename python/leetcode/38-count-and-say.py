#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 报数 简单

'''
https://leetcode-cn.com/problems/count-and-say/
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。



示例 1:

输入: 1
输出: "1"
示例 2:

输入: 4
输出: "1211"
'''

class Solution:
    def countAndSay(self, n: int) -> str:
        def next(ss):
            res = ""
            count = 1
            a = ss[0]
            for i in range(1, len(ss)):
                if ss[i] == ss[i - 1]:
                    count += 1
                else:
                    res = '{}{}{}'.format(res, count, a)
                    count = 1
                    a = ss[i]
            res += str(count) + a
            return res
        res = "1"
        for i in range(1, n):
            res = next(res)
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
        self.assertEqual(func(1), "1")
        self.assertEqual(func(2), "11")
        self.assertEqual(func(3), "21")
        self.assertEqual(func(4), "1211")
        self.assertEqual(func(5), "111221")
        pass

    def test_func(self):
        self.do(s.countAndSay)

if __name__ == "__main__":
    unittest.main()
