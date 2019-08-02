#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 括号生成

'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''

class Solution:
    def generateParenthesis(self, n: int):
        def _make_next(pts):
            res = []
            for p in pts:
                res.append(p + '()')
                res.append('()' + p)
                res.append('(' + p + ')')
            #  print(len(res), res)
            #  return list(set(res))
            return res
        pts_total = [['()']]
        if len(pts_total) < n:
            for i in range(len(pts_total), n):
                now = _make_next(pts_total[i - 1])
                now.remove('()'* (i + 1))
                pts_total.append(now)
        return pts_total[n-1]

s = Solution()

if __name__ == "__main__":
    for i in range(1, 5):
        res = s.generateParenthesis(i)
        print(len(res), res)
