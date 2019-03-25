#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 整数翻转

'''

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321

示例 2:

输入: -123
输出: -321

示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''

import unittest
import time

MAX = 2 ** 31 - 1
MIN = -2 ** 31

# 这是最简单的字符串翻转 平均 40 ms
def reverse1(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return 0
    y = ""
    r = 0
    a = str(x)
    length = len(a)
    for i in range(length):
        index = length - 1 - i
        if not y and a[index] == "0":
            continue
        y += a[index]
    if y[-1] == "-":
        r = -int(y[0:-1])
        if r < MIN:
            return 0
        return r
    r = int(y)
    if r > MAX:
        return 0
    return r

MAX_R = (MAX - 7) // 10
MIN_R = (MIN - -8) // 10
'''使用数学的方式进行翻转，原理是除以 10 取余，推到前面，
需要注意的是 Python 中 // 会四舍五入 平均 36 ms'''
def reverse2(x):
    """
    :type x: int
    :rtype: int
    """
    rev = 0
    while x != 0:
        chu = 10
        if x < 0:
            chu = -10
        pre = x % chu
        x = (x - pre) // 10
        if rev > MAX_R or (rev == MAX_R and pre == 7):
            return 0
        if rev < MIN_R or (rev == MIN_R and pre == -8):
            return 0
        rev = rev * 10 + pre
    return rev

class TestMain(unittest.TestCase):

    def test_reverse1(self):
        self.assertEqual(reverse1(123), 321)
        self.assertEqual(reverse1(-123), -321)
        self.assertEqual(reverse1(-12300), -321)
        self.assertEqual(reverse1(1534236469), 0)
        self.assertEqual(reverse1(-1563847412), 0)
        self.assertEqual(reverse1(0), 0)

    def test_reverse2(self):
        self.assertEqual(reverse2(123), 321)
        self.assertEqual(reverse2(-123), -321)
        self.assertEqual(reverse2(-12300), -321)
        self.assertEqual(reverse2(1534236469), 0)
        self.assertEqual(reverse2(-1563847412), 0)
        self.assertEqual(reverse2(0), 0)

def func_time(func, *args):
    b = time.clock()
    count = 1000
    for i in range(count):
        func(*args)
    print(time.clock() - b)

if __name__ == "__main__":
    #  s = Solution()
    #  print(s.reverse(123) == 321)
    #  print(s.reverse(-123) == -321)
    #  print(s.reverse(-12300) == -321)
    #  print(s.reverse(0) == 0)
    #  print(s.reverse(1534236469) == 0)
    #  print(s.reverse(-1563847412) == 0)
    #  func_time(reverse2, 1534236469)
    #  func_time(reverse1, 1534236469)
    unittest.main()
