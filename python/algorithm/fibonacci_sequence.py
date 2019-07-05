#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 斐波那契数列

def fibonacci_recursive(n):
    '''
    递归的方式，理解简单，不会在真实开发中用到
    '''
    if n < 3:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_for(n):
    '''
    使用 for 循环挨个计算，减少了递归中的重复计算
    时间复杂度 O(n)
    空间复杂度 O(1)
    '''
    if n < 3:
        return 1
    n1, n2 = 1, 1
    n3 = 0
    for i in range(3, n + 1):
        n3 = n1 + n2
        n1, n2 = n2, n3
    return n3

nums = [1, 1]
def fibonacci_array(n):
    '''
    for 循环的方式已经很快了，但是如果想要获取多个值时，每次都要从头计算
    这时候我们可以把计算的结果保存起来，下次可以直接使用，这是一种空间换时间的算法。
    时间复杂度 O(n)
    空间复杂度 O(n)
    '''
    if len(nums) < n:
        for i in range(len(nums), n):
            nums.append(nums[i - 1] + nums[i - 2])
    return nums[n - 1]

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
        n = 8
        res = 21
        self.assertEqual(func(n), res)
        pass

    def test_func(self):
        self.do(fibonacci_recursive)
        self.do(fibonacci_for)
        self.do(fibonacci_array)

if __name__ == "__main__":
    unittest.main()

