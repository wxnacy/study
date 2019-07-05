#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:  改进的装饰器
# 使用 functools.wraps 装饰器可以把 func 的相关属性复制到 clocked 中
# 使用递归实现斐波那契数列非常耗时，会有很多重复计算函数

import time
from functools import wraps

def clock(func):
    @wraps(func)
    def clocked(*args, **kwargs):
        '''计时'''
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print(f'[{elapsed:0.8f}s] {func.__name__}({args}, {kwargs}) -> {result}')
        return result
    return clocked

@clock
def f1(n):
    '''斐波那契数列'''
    return n if n < 3 else f1(n-1) + f1(n-2)

if __name__ == "__main__":
# [0.00000049s] f1((2,), {}) -> 2
# [0.00000042s] f1((1,), {}) -> 1
# [0.00003052s] f1((3,), {}) -> 3
# [0.00000028s] f1((2,), {}) -> 2
# [0.00003689s] f1((4,), {}) -> 5
# [0.00000032s] f1((2,), {}) -> 2
# [0.00000027s] f1((1,), {}) -> 1
# [0.00000547s] f1((3,), {}) -> 3
# [0.00004824s] f1((5,), {}) -> 8
    print(f1(5))        # 8
    print(f1)           # <function f1 at 0x10831a0d0>
    print(f1.__name__)  # f1
    print(f1.__doc__)   # 斐波那契数列



