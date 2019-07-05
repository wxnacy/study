#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 使用生成器函数创建生成器


def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index


if __name__ == "__main__":
    ap = aritprog_gen(0, 2, 7)
    print(list(ap)) # [0, 2, 4, 6]
