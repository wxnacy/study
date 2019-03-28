#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 有效的括号

'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
'''

BRACKETS = {
    ")": "(",
    "}": "{",
    "]": "[",
}

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for c in s:
        if c not in BRACKETS:
            stack.append(c)
        else:
            cr = BRACKETS[c]
            if not stack:
                return False
            if stack[-1] != cr:
                return False
            else:
                stack.pop()
    return stack == []

import unittest

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def do(self, func):
        self.assertFalse(func("[)"))
        self.assertTrue(func("[]"))
        self.assertTrue(func(""))
        self.assertTrue(func("()[]{}"))
        self.assertFalse(func("[()"))
        self.assertFalse(func("(])"))
        self.assertFalse(func("([)])"))
        self.assertFalse(func("(()("))
        self.assertFalse(func("([)]"))
        self.assertFalse(func("]"))
        self.assertFalse(func("()]"))
        self.assertTrue(func("{[]}"))
        self.assertTrue(func("(([]){})"))

    def test_func1(self):
        self.do(isValid)

if __name__ == "__main__":
    import utils
    count = 10000
    utils.print_func_run_time(count, isValid, s = "(([]){})")
    unittest.main()
