#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

count = 0
def search(l, val):
    low = 0
    high = len(l) - 1
    global count
    while low <= high:
        mid = (high - low) // 2
        count += 1
        if l[mid] == val:
            return mid
        elif l[mid] < val:
            low = mid+1
        elif l[mid] > val:
            high = mid - 1
    return

if __name__ == "__main__":
    index = search(list(range(240)), 0)
    print(index)
    print(count)
