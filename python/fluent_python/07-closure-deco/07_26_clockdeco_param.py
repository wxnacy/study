#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:  计时器参数化装饰器版本

import timeit
import time

FMT='[{T:0.8f}s] {F} -> {R}'

def clock(fmt=FMT):
    def clocked(func):
        def _clock(*args, **kw):
            t0 = timeit.default_timer()
            result = func(*args, **kw)
            R = repr(result)
            T = timeit.default_timer() - t0
            F = func.__name__
            print(fmt.format(**locals()))
            return result
        return _clock
    return clocked

@clock()
def snooze(s):
    time.sleep(s)

if __name__ == "__main__":
    snooze(.321)    # [0.32474239s] snooze -> None
