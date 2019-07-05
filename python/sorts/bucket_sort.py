#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 桶排序，内部使用插入排序

import time
import random
import utils
from insertion_sort import insertion_sort

def bucket_sort(nums: list, bucket_size = 5):
    '''
    使用字典来储存桶
    '''
    min_num, max_num = min(nums), max(nums)
    bucket_count = ( max_num - min_num ) // bucket_size + 1
    buckets = {i : [] for i in range(bucket_count)}
    for n in nums:
        i = (n - min_num) // bucket_size
        buckets[i].append(n)
    res = []
    for i in range(len(buckets)):
        insertion_sort(buckets[i])
        res.extend(buckets[i])
    return res

def bucket_sort_array(nums: list, bucket_size = 5):
    '''
    使用数组来储存桶，通常比字典的方式要快一点
    bucket_size 为每个桶内的最大元素数
    '''
    min_num, max_num = min(nums), max(nums)     # 获取最大、最小值
    bucket_count = ( max_num - min_num ) // bucket_size + 1 # 计算桶的大小
    buckets = [[] for i in range(bucket_count)] # 初始化空桶
    for n in nums:
        i = (n - min_num) // bucket_size
        buckets[i].append(n)                    # 将数字分配到相应的桶中
    res = []
    for b in buckets:
        insertion_sort(b)                       # 将每个桶进行插入排序
        res.extend(b)                           # 将每个桶进行拼装
    return res

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
        for k, v in utils.generate_randoms(10):
            self.assertEqual(func(k), v)

    def test_func(self):
        self.do(bucket_sort)
        self.do(bucket_sort_array)

if __name__ == "__main__":

    unittest.main()
