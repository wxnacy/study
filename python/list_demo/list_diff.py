#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 列表的交集、并集、差集

import random

def rand_int_arr(length):
    arr = []
    for i in range(length):
        r = random.randrange(19)
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
    a = rand_int_arr(10)
    b = rand_int_arr(10)
    print(a)
    print(b)
    r1 = intersection1(a, b)
    print('交集：使用列表解析', r1)
    r2 = intersection2(a, b)
    print('交集：使用自带函数', r2)
    r3 = union1(a, b)
    print('并集：使用列表相加', r3)
    r4 = union2(a, b)
    print('并集：使用自带函数', r4)
    r5 = difference1(a, b)
    print('差集：使用列表解析', r5)
    r6 = difference2(a, b)
    print('差集：使用自带函数', r6)

    # [5, 8, 13, 0, 7, 16, 13, 2, 2, 7]
    # [11, 10, 6, 17, 7, 13, 2, 16, 10, 13]
    # 交集：使用列表解析 [16, 2, 13, 7]
    # 交集：使用自带函数 [16, 2, 13, 7]
    # 并集：使用列表相加 [0, 2, 5, 6, 7, 8, 10, 11, 13, 16, 17]
    # 并集：使用自带函数 [0, 2, 5, 6, 7, 8, 10, 11, 13, 16, 17]
    # 差集：使用列表解析 [8, 0, 5]
    # 差集：使用自带函数 [0, 8, 5]

