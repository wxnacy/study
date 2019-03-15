#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 列表的交集、并集、差集

import random
import time

def rand_int_arr(length):
    arr = []
    for i in range(length):
        r = random.randrange(10000)
        arr.append(r)
    return arr

def intersection1(a, b):
    '''交集：使用列表解析'''
    return list(set([i for i in a if i in b]))

def intersection2(a, b):
    '''交集：使用自带函数'''
    return list(set(a).intersection(set(b)))

def union1(a, b):
    '''并集：使用列表相加'''
    return list(set(a + b))

def union2(a, b):
    '''并集：使用自带函数'''
    return list(set(a).union(set(b)))

def difference1(a, b):
    '''差集：使用列表解析'''
    return list(set([i for i in a if i not in b]))

def difference2(a, b):
    '''差集：使用自带函数'''
    return list(set(a).difference(set(b)))


if __name__ == "__main__":
    a = rand_int_arr(10000)
    b = rand_int_arr(10000)
    begin = time.clock()
    r1 = intersection1(a, b)
    print('交集：使用列表解析', time.clock() - begin)
    begin = time.clock()
    r2 = intersection2(a, b)
    print('交集：使用自带函数', time.clock() - begin)
    begin = time.clock()
    r3 = union1(a, b)
    print('并集：使用列表相加', time.clock() - begin)
    begin = time.clock()
    r4 = union2(a, b)
    print('并集：使用自带函数', time.clock() - begin)
    begin = time.clock()
    r5 = difference1(a, b)
    print('差集：使用列表解析', time.clock() - begin)
    begin = time.clock()
    r6 = difference2(a, b)
    print('差集：使用自带函数', time.clock() - begin)

#  交集：使用列表解析 0.9532590000000001
#  交集：使用自带函数 0.002062999999999926
#  并集：使用列表相加 0.0010879999999999779
#  并集：使用自带函数 0.0022370000000000445
#  差集：使用列表解析 0.9966799999999998
#  差集：使用自带函数 0.0014449999999999186

