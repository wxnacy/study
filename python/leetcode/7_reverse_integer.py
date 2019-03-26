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
import utils

MAX = 2 ** 31 - 1
MIN = -2 ** 31

# 这是最简单的字符串翻转 平均 40 ms
def reverse1(x):
    """
    先转换字符串、在循环倒装，最后转为 int
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

def reverse2(x):
    """
    使用取余的方式，弹出 x 的最后一位，并推到 r 的后面，并如此往复，直到 x = 0
    :type x: int
    :rtype: int
    """
    r = 0
    while x != 0:
        chu = 10
        if x < 0:           # 根据整数的正负，使用相应的取余除数
            chu = -10
        pre = x % chu       # 弹出 x 的最后一位
        x = (x - pre) // 10 # 取余完毕后，整数减去一位
        if r > MAX_R or (r == MAX_R and pre == 7):
            # MAX_R = 2147483640
            # 此处防止后续推入 pre 时，整数溢出
            return 0
        if r < MIN_R or (r == MIN_R and pre == -8):
            # MIN_R = -2147483648
            # 此处防止后续推入 pre 时，整数溢出
            return 0
        r = r * 10 + pre    # 将弹出的最后一位，推到 r 的后面
    return r

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

def func_time(count, func, **kw):
    b = time.clock()
    for i in range(count):
        func(**kw)
    print(func.__name__, 'run {} times used {}s'.format(count, time.clock() -b ))

if __name__ == "__main__":
    count = 10000
    #  utils.print_func_run_time(count, reverse1, x=1534236469)
    #  utils.print_func_run_time(count, reverse2, x=1534236469)
    utils.print_func_run_time(count, reverse1, x=123000)
    utils.print_func_run_time(count, reverse2, x=123000)
    unittest.main()
