#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 最后一个单词的长度 简单

'''
https://leetcode-cn.com/problems/length-of-last-word/
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''
        时间复杂度 O(n)
        执行用时 : 40 ms, 在Length of Last Word的Python3提交中击败了98.61% 的用户
        内存消耗 : 13.1 MB, 在Length of Last Word的Python3提交中击败了86.41% 的用户
        '''
        leng = 0
        for j in range(len(s)):
            i = len(s) - j - 1
            if s[i] == ' ':
                if leng > 0:
                    return leng
                leng = 0
            else:
                leng += 1
        return leng
        

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
        self.assertEqual(func("Hello World"), 5)
        self.assertEqual(func("World"), 5)
        self.assertEqual(func(" "), 0)
        self.assertEqual(func(""), 0)
        self.assertEqual(func("a "), 1)
        self.assertEqual(func(" a"), 1)
        pass

    def test_func(self):
        self.do(s.lengthOfLastWord)

if __name__ == "__main__":
    unittest.main()
