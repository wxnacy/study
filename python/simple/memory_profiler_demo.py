#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 使用 memory_profiler 分析内存使用情况
# 博客地址：


from memory_profiler import profile

@profile
def test1():
    c = []
    a = [1, 2, 3] * (2 ** 20)
    b = [1] * (2 ** 20)
    c.extend(a)
    c.extend(b)
    del b
    del c


@profile()
def test2():
    c = []
    c.extend([1, 2, 3] * (2 ** 20))
    c.extend([1] * (2 ** 20))

@profile(precision=4, stream=open('/tmp/memory_profiler.log','w+'))
def test3():
    a = [1, 2] * (2 ** 10)

if __name__ == "__main__":
    test1()
    #  test2()
    #  test3()
