#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:  简单的装饰器
# 方法的属性会被覆盖掉

import time

def clock(func):
    def clocked(*args):
        '''计时'''
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        print(f'[{elapsed:0.8f}s] {func.__name__}({args}) -> {result}')
        return result
    return clocked

@clock
def f1(n):
    return n if n < 3 else f1(n-1) + f1(n-2)

if __name__ == "__main__":
    # [0.00000080s] f1((2,)) -> 2
    print(f1(2))        # 2
    print(f1)           # <function clock.<locals>.clocked at 0x10bb5a158>
    print(f1.__name__)  # clocked
    print(f1.__doc__)   # 计时



