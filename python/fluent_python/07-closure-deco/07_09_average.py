#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        return sum(series) / len(series)
    return averager



if __name__ == "__main__":
    avg = make_averager()
    print(avg(10))  # 10.0
    print(avg(11))  # 10.5
    print(avg(12))  # 11.0
    print(dir(avg.__code__))
    print(avg.__code__.co_varnames) # 局部变量 ('new_value',)
    print(avg.__code__.co_freevars) # 自由变量 ('series',)
    print(avg.__closure__)          # (<cell at 0x106c726a8: list object at 0x106ed0188>,)
    print(avg.__closure__[0].cell_contents) # [10, 11, 12]
