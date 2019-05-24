#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:
# 10 个台阶，可以一次 1 个台阶，或者 2 个台阶，或者 3 个台阶，总共有多少种可能
# 使用递归

def step(n):
    if n <=3:
        return n
    else:
        return step(n - 1) + step(n - 2) + step(n - 3)


if __name__ == "__main__":
    res = step(10)
    print(res)
