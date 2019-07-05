#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager

if __name__ == "__main__":
    avg = make_averager()
    print(avg(10))  # 10.0
    print(avg(11))  # 10.5
    print(avg(12))  # 11.0
