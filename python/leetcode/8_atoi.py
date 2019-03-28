#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 字符串转换整数 (atoi)

'''
请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，qing返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

示例 1:

输入: "42"
输出: 42
示例 2:

输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
示例 3:

输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
示例 4:

输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
示例 5:

输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
     因此返回 INT_MIN (−231) 。
'''

MAX = 2 ** 31 -1
MIN = -2 ** 31

NUMBERS1 = ["1", "2", '3', '4', '5', '6', '7', '8', '9']
NUMBERS2 = ["1", "2", '3', '4', '5', '6', '7', '8', '9', '0']

def myAtoi1(s):
    """
    :type s: str
    :rtype: int
    """
    r = 0
    sym = ''
    zero_count = 0
    for c in s:
        if c == '0':
            zero_count += 1
        if c in ('+', '-', ' ') and zero_count > 0:
            return 0
        if c in (' ', '0') and r == 0 and not sym:
            continue
        elif c in ('0') and r == 0 and sym:
            continue
        elif c in (' ', '+', '-') and r == 0 and sym:
            return 0
        elif c in ('+', '-') and r == 0 and not sym:
            sym = c
        elif (c in NUMBERS1 and r == 0) or (c in NUMBERS2 and r > 0):
            r = r * 10 + int(c)
            if (not sym or sym == '+') and r >= MAX:
                return MAX
            if sym == '-' and -r <= MIN:
                return MIN
        elif c not in NUMBERS2 and r > 0:
            return -r if sym == '-' else r
        else:
            return 0
    return -r if sym == '-' else r

import re
def myAtoi2( s):
        a = ''.join(re.findall(r'^[-+]{0,1}\d+', s.strip()))
        # 当a为空字符串返回0
        if not a:
            return 0
        a = int(a)
        b = 2 ** 31
        if a > b - 1:
            return b - 1
        elif a < -b:
            return -b
        else:
            return a

import unittest

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def do(self, func):
        self.assertEqual(func("42"), 42)
        self.assertEqual(func("   -42"), -42)
        self.assertEqual(func("4193 with words"), 4193)
        self.assertEqual(func("words and 987"), 0)
        self.assertEqual(func("   +0 123"), 0)
        self.assertEqual(func("+-2"), 0)
        self.assertEqual(func("0-1"), 0)
        self.assertEqual(func("-91283472332"), MIN)
        self.assertEqual(func("912834723320"), MAX)
        self.assertEqual(func("  0000000000012345678"), 12345678)
        self.assertEqual(func("-000000000000001"), -1)
        self.assertEqual(func("  -0012a42"), -12)
        self.assertEqual(func("-   234"), 0)
        self.assertEqual(func("    -88827   5655  U"), -88827)

    def test_func(self):
        self.do(myAtoi1)
        self.do(myAtoi2)

if __name__ == "__main__":
    import utils
    count = 1000
    utils.print_func_run_time(count, myAtoi1, s = "4193 with words")
    utils.print_func_run_time(count, myAtoi2, s = "4193 with words")

    unittest.main()
