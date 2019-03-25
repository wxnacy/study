#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 最长公共前缀

"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

"""

# 使用逐个比较 平均 44 ms 比较慢
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        m = {}
        i = 1
        j = 0
        while i < len(strs):
            f = strs[0]
            if j >= len(f):
                break
            r = strs[i]
            le = len(f) - j
            if f[0:le] == r[0:le]:
                i += 1
            else:
                i = 1
                j += 1
        f = strs[0]
        res = f[0:len(f) - j]
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]) == "fl")
    print(s.longestCommonPrefix(["dog","racecar","car"]) == "")
    print(s.longestCommonPrefix([]) == "")
    print(s.longestCommonPrefix(["a"]) == "a")
    print(s.longestCommonPrefix(["a", "a"]) == "a")
