#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import random
import timeit

def generate_random_ints(length: int):
    return [random.randint(0, length) for i in range(length)]

def generate_random(i=100):
    nums = generate_random_ints(i)
    res = list(nums)
    nums.sort()
    return res, nums

randoms = [(generate_random(i)) for i in range(50, 200)]

def generate_randoms(begin=50, end=100):
    return [(generate_random(i)) for i in range(begin, end)]


def print_unittest_do_run_time(count, do_func, test_func):
    '''
    打印测试用例 do 方法所需的时间
    '''
    b = timeit.default_timer()
    for i in range(count):
        do_func(test_func)
    t = timeit.default_timer() - b
    print('{} run {} times used {}s'.format(
        test_func.__name__.ljust(20), count, t))

def print_func_run_time(count, func, *args):
    b = timeit.default_timer()
    for i in range(count):
        func(*args)
    t = timeit.default_timer() - b
    print('{} run {} times used {}s'.format(
        func.__name__.ljust(20), count, t))
    return func.__name__, t

if __name__ == "__main__":
    arr = generate_random_ints(10)
    print(arr)
    arr.sort()
    print(arr)
