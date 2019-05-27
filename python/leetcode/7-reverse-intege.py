#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 整数反转

'''
难度：简单

知识点：数学

地址：[https://leetcode-cn.com/problems/reverse-integer/](https://leetcode-cn.com/problems/reverse-integer/)

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

    假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

'''

class Solution:

    MAX = 2 ** 31 - 1
    MIN = -2 ** 31

    def reverse(self, x: int) -> int:
        '''
        时间复杂度 O(logn)
        空间复杂度 O(1)
        执行用时 : 44 ms, 在Reverse Integer的Python3提交中击败了99.13% 的用户
        内存消耗 : 13.1 MB, 在Reverse Integer的Python3提交中击败了94.93% 的用户
        '''
        if x == 0:
            return 0
        y = ""
        rev = 0
        a = str(x)
        length = len(a)
        for i in range(length):
            index = length - 1 - i
            if not y and a[index] == "0":
                continue
            y += a[index]
        if y[-1] == "-":
            rev = -int(y[0:-1])
            if rev < self.MIN:
                return 0
            return rev
        rev = int(y)
        if rev > self.MAX:
            return 0
        return rev

    def reverse1(self, x: int) -> int:
        '''
        弹出和推入数字
        时间复杂度 O(logn)
        空间复杂度 O(1)
        执行用时 : 48 ms, 在Reverse Integer的Python3提交中击败了98.06% 的用户
        内存消耗 : 13 MB, 在Reverse Integer的Python3提交中击败了99.21% 的用户
        '''
        rev = 0
        div = 10 if x > 0 else -10  # 如果数字为负，div 也要为负
        max_r = (self.MAX - 7) // 10
        min_r = (self.MIN + 8) // 10
        while x != 0:
            pop = x % div           # x 取余，pop 就是要推出的数字
            rev = rev * 10 + pop    # 将 pop 推到 r 的后面
            x = ( x - pop ) // 10   # 推出 pop 后 x 应该等于的数字
            # 防止整数溢出
            if rev > max_r or (rev == max_r and pop > 7):
                return 0
            if rev < min_r or (rev == min_r and pop < -8):
                return 0
        return rev

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
        self.assertEqual(func(123), 321)
        self.assertEqual(func(-123), -321)
        self.assertEqual(func(120), 21)
        self.assertEqual(func(-12300), -321)
        self.assertEqual(func(1534236469), 0)
        self.assertEqual(func(-1563847412), 0)
        self.assertEqual(func(0), 0)
        pass

    def test_func(self):
        self.do(s.reverse)

if __name__ == "__main__":
    import utils
    count = 300
    tm = TestMain()
    utils.print_unittest_do_run_time(count, tm.do, s.reverse)
    utils.print_unittest_do_run_time(count, tm.do, s.reverse1)
    unittest.main()

