#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import random_util
import time

def quick_sort(arr: list):

    def partition(arr, left, right):
        t = arr[left]                       # 找出想要作为分割位的中间值
        x = left                            # 将左侧坐标重新初始化
        y = right                           # 将右侧坐标重新初始化
        while x < y:                        # 完成一次左右坐标相遇
            while x < y and arr[y] >= t:    # 先从右侧查找一次小于中间值的数字
                y -= 1
            arr[x] = arr[y]                 # 将找到的数字赋值到左坐标的位置
            while x < y and arr[x] <= t:    # 先从左侧查找一次大于中间值的数字
                x += 1
            arr[y] = arr[x]                 # 将找到的数字赋值到空出的右侧坐标位

        arr[x] = t                          # 将中间值赋值到最后空出位置上
        return x                            # 返回此次最终的中间位置

    def _sort(arr, left, right):
        if left < right:
            index = partition(arr, left, right) # 将数组做第一次分治
            _sort(arr, left, index - 1)         # 将左侧数据做下一步分治
            _sort(arr, index + 1, right)        # 将右侧数据做下一步分治


    _sort(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    arr = random_util.rand_int_arr(10)
    print(arr)
    quick_sort(arr)
    print(arr)
