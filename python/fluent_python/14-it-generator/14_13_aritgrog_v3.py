#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 使用生成器函数创建生成器

import itertools

def aritprog_gen(begin, step, end=None):
    ap_gen = itertools.count(begin, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda x: x < end, ap_gen)
    return ap_gen


if __name__ == "__main__":
    ap = aritprog_gen(0, 2, 7)
    print(list(ap)) # [0, 2, 4, 6]
