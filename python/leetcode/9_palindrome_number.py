#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 回文数

def isPalindrome1(x):
    """
    :type x: int
    :rtype: bool
    """
    if x == 0:
        return True
    if x < 0:
        return False
    if x % 10 == 0:
        return False
    a = str(x)
    i = 0
    j = len(a) - 1
    while i <= j:
        if a[i] != a[j]:    # 从头尾逐个对比，直到坐标相遇
            return False
        i += 1
        j -= 1
    return True

def isPalindrome2(x):
    """
    依然是数学的方式 平均 116 ms
    :type x: int
    :rtype: bool
    """
    if x == 0:
        return True
    if x < 0:
        return False
    if x % 10 == 0:     # 10 倍数肯定不是回文数
        return False
    temp = 0
    while x > temp:
        pre = x % 10
        x  = (x - pre) // 10
        temp = temp * 10 + pre
    # x == temp 代表数字为偶数长度
    # x == temp // 10 代表数字为奇数长度
    return x == temp or x == temp // 10

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
        self.assertTrue(func(121))
        self.assertTrue(func(0))
        self.assertTrue(func(6))
        self.assertTrue(func(11))

    def test_func1(self):
        self.do(isPalindrome1)

    def test_func2(self):
        self.do(isPalindrome2)

if __name__ == "__main__":
    count = 100000
    utils.print_func_run_time(count, isPalindrome1, x = 123454321)
    utils.print_func_run_time(count, isPalindrome2, x = 123454321)
    unittest.main()

# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK
# isPalindrome1 run 100000 times used 0.142989s
# isPalindrome2 run 100000 times used 0.143997s

# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK
# isPalindrome1 run 100000 times used 0.142461s
# isPalindrome2 run 100000 times used 0.140228s
