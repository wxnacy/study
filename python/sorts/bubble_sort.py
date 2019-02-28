#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from random_util import rand_int_arr

def bubble_sort(arr):
    leng = len(arr)

    def _temp(x, y):
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp

    for i in range(leng):
        for j in range(i + 1, leng):
            if arr[i] > arr[j]:
                _temp(i, j)

if __name__ == "__main__":
    arr = rand_int_arr(10)
    print(arr)
    bubble_sort(arr)
    print(arr)
