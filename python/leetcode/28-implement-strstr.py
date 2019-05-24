#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 实现strStr()

'''
https://leetcode-cn.com/problems/implement-strstr/
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
'''

class Solution:
    def strStr(self, t: str, p: str) -> int:
        if not p:
            return 0
        prefix = self.make_prefix(p)
        i = 0
        j = 0
        len_p = len(p)
        while i < len(t) and j < len_p:
            if j == -1 or t[i] == p[j]:
                i += 1
                j += 1
            else:
                j = prefix[j]
        if j == len_p:
            return i - j
        return -1


    def make_prefix(self, p: str):
        l = len(p)
        i = 0
        j = -1
        prefix = [0] * l
        prefix[0] = -1
        while i < l - 1:
            if j == -1 or p[i] == p[j]:
                i += 1
                j += 1
                prefix[i] = j
            else:
                j = prefix[j]
        return prefix

s = Solution()

import unittest
import utils
import timeit

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def do(self, func):
        '''todo'''
        self.assertEqual(func("hello", "ll"), 2)
        self.assertEqual(func("aaaaa", "bba"), -1)
        self.assertEqual(func("aaaac", "aac"), 2)
        pass

    def test_func(self):
        self.do(s.strStr)

        self.assertEqual(s.make_prefix("abc"), [-1, 0, 0])
        self.assertEqual(s.make_prefix("aac"), [-1, 0, 1])
        self.assertEqual(s.make_prefix("ababc"), [-1, 0, 0, 1, 2])

if __name__ == "__main__":
    count = 100000
    t = "ababcabcde"
    p = "abcd"
    utils.print_func_run_time(count, s.strStr, t = t, p = p)
    b = timeit.default_timer()
    for i in range(count):
        t.index(p)
    print(timeit.default_timer() - b)
    unittest.main()


