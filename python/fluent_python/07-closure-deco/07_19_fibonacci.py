#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:  改进的装饰器
# 使用递归实现斐波那契数列非常耗时，会有很多重复计算函数
# 使用 functools.lru_cache(maxsize, typed) 装饰器起到缓存的作用
# maxsize参数指定存储多少个调用的结果。缓存满了之后，旧的结果会被扔掉，腾出空间。
# 为了得到最佳性能，maxsize应该设为2的幂。
# typed参数如果设为True，把不同参数类型得到的结果分开保存，
# 即把通常认为相等的浮点数和整数参数（如1和1.0）区分开。

import time
from functools import wraps
from functools import lru_cache

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

@lru_cache(maxsize=128, typed=True)    # 必须放在最外层
@clock
def f1(n):
    '''斐波那契数列'''
    return n if n < 3 else f1(n-1) + f1(n-2)

if __name__ == "__main__":
# [0.00000053s] f1((2,), {}) -> 2
# [0.00000041s] f1((1,), {}) -> 1
# [0.00003426s] f1((3,), {}) -> 3
# [0.00003875s] f1((4,), {}) -> 5
# [0.00004331s] f1((5,), {}) -> 8
    print(f1(5))        # 8
    print(f1)           # <functools._lru_cache_wrapper object at 0x1042ef240>
    print(f1.__name__)  # f1
    print(f1.__doc__)   # 斐波那契数列
    print(f1.__code__)



