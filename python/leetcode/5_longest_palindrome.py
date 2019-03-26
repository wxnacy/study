#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 最长回文子串

'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''
def longestPalindrome1(self, s):
    """
    :type s: str
    :rtype: str
    """
    l = ""
    str_index = {}
    for j in range(s):
        a = s[j]
        if a in str_index:
            i = str_index[a]
            if j - i 


        str_index[a] = j

#  def isPalindrome2(x):
    #  """
    #  依然是数学的方式 平均 116 ms
    #  :type x: int
    #  :rtype: bool
    #  """
    #  if x == 0:
        #  return True
    #  if x < 0:
        #  return False
    #  if x % 10 == 0:     # 10 倍数肯定不是回文数
        #  return False
    #  temp = 0
    #  while x > temp:
        #  pre = x % 10
        #  x  = (x - pre) // 10
        #  temp = temp * 10 + pre
    #  # x == temp 代表数字为偶数长度
    #  # x == temp // 10 代表数字为奇数长度
    #  return x == temp or x == temp // 10

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
        self.assertEqual(func("babad"), "bab")
        self.assertEqual(func("cbbd"), "bb")

    def test_func1(self):
        self.do(longestPalindrome1)

    #  def test_func2(self):
        #  self.do(isPalindrome2)

if __name__ == "__main__":
    #  count = 100000
    #  utils.print_func_run_time(count, isPalindrome1, x = 123454321)
    #  utils.print_func_run_time(count, isPalindrome2, x = 123454321)
    unittest.main()
