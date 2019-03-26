#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 无重复字符的最长子串

'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''

# 遍历一次，逐个对比当前字母是否出现在前面的字符串中，如果有，从存在处的坐标重
# 新开始计算 平均 96 秒 偏慢
def lengthOfLongestSubstring1(s):
    """
    :type s: str
    :rtype: int
    """
    s1 = ""
    count = 0
    max_count = 0
    for a in s:
        if a not in s1:
            s1 += a
            count += 1
        else:
            if count > max_count:
                max_count = count
            s1 = s1[s1.index(a, 0, len(s1)) + 1:] + a
            count = len(s1)
    return max_count if max_count > count else count

#  class Solution(object):
    #  def lengthOfLongestSubstring(self, s):
        #  """
        #  :type s: str
        #  :rtype: int
        #  """
        #  s1 = ""
        #  count = 0
        #  max_count = 0
        #  i = 0
        #  j = 0
        #  sets = set()
        #  l = len(s)
        #  while i < l and j < l:
            #  if s[j] not in sets:
                #  sets.add(s[j])
                #  j += 1
                #  max_count = max(max_count, j - i)
            #  else:
                #  sets.remove(s[i])
                #  i += 1
        #  return max_count

def lengthOfLongestSubstring2(s):
    """
    :type s: str
    :rtype: int
    """
    str_index = {}
    i = 0
    length = 0
    for j in range(len(s)):
        js = s[j]
        if js in str_index:
            i = max(i, str_index[js] + 1)
        length = max(length, j - i + 1)
        str_index[js] = j
    return length


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
        self.assertEqual(func("adbabcbb"), 3)
        self.assertEqual(func("bbbbb"), 1)
        self.assertEqual(func("pwwkew"), 3)
        self.assertEqual(func(" "), 1)
        self.assertEqual(func("aab"), 2)
        self.assertEqual(func("dvdf"), 3)
        self.assertEqual(func("aabaab!bb"), 3)

    def test_func1(self):
        self.do(lengthOfLongestSubstring1)

    def test_func2(self):
        self.do(lengthOfLongestSubstring2)

if __name__ == "__main__":
    count = 10000
    utils.print_func_run_time(count, lengthOfLongestSubstring1, s = "aabaab!bb")
    utils.print_func_run_time(count, lengthOfLongestSubstring2, s = "aabaab!bb")
    unittest.main()

