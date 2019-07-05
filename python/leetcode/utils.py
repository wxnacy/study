#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import timeit
import random

def print_func_run_time(count, func, **kw):
    b = timeit.default_timer()
    for i in range(count):
        func(**kw)
    print('{} run {} times used {}s'.format(
        func.__name__.ljust(20),
        count,
        timeit.default_timer() -b ))


#  CLOCK_FMT = '[{T:0.8f}s] {F}({A}, {K}) -> {R}'
CLOCK_FMT = '[{T:0.8f}s] {F}() -> {R}'
def clock(times=1, fmt=CLOCK_FMT, logger_func=print):
    def clock_wraper(func):
        def _wraper(*args, **kwargs):
            t0 = timeit.default_timer()
            result = None
            for i in range(times):
                result = func(*args, **kwargs)
            T = timeit.default_timer() - t0
            F = func.__name__
            A = args
            K = kwargs
            R = repr(result)
            logger_func(fmt.format(**locals()))
            return result
        return _wraper
    return clock_wraper

#  def print_func_run_time1(count, func, *args):
    #  b = timeit.default_timer()
    #  for i in range(count):
        #  func(*args)
    #  print('{} {} run {} times used {}s'.format(
        #  func.__name__.ljust(2), args,
        #  count,
        #  timeit.default_timer() -b ))

def print_unittest_do_run_time(count, do_func, test_func):
    '''
    打印测试用例 do 方法所需的时间
    '''
    b = timeit.default_timer()
    for i in range(count):
        do_func(test_func)
    print('{} run {} times used {}s'.format(
        test_func.__name__.ljust(20),
        count,
        timeit.default_timer() -b ))

class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

def array2listnode(arr: list):
    '''数组转为链表'''
    ln = ListNode(0)
    l = ln
    for i in arr:
        l.next = ListNode(i)
        l = l.next
    return ln.next

def listnode2array(ln: ListNode):
    '''链表转为数组'''
    arr = []
    while ln:
        arr.append(ln.val)
        ln = ln.next
    return arr


def get_many_random_arr_int(count):
    res = []
    for i in range(count):
        items = []
        for j in range(i):
            items.append(random.randint(-j, j))

        res.append(items)
    return res



if __name__ == "__main__":
    print_func_run_time1(1, get_many_random_arr_int, 300)
    #  res = get_many_random_arr_int(100)

    #  print(res)
