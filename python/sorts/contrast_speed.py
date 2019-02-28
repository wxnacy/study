#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from quick_sort import quick_sort
from bubble_sort import bubble_sort
from random_util import rand_int_arr
import time


if __name__ == "__main__":
    length = 1000
    print('长度为 {} 的随机数数组排序时长对比'.format(length))
    arr = rand_int_arr(length)
    b = time.clock()
    arr.sort()
    print('arr.sort()\t', time.clock() - b)

    arr = rand_int_arr(length)
    b = time.clock()
    quick_sort(arr)
    print('quick_sort()\t', time.clock() - b)

    arr = rand_int_arr(length)
    b = time.clock()
    bubble_sort(arr)
    print('bubble_sort()\t', time.clock() - b)
