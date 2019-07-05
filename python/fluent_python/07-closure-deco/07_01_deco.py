#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 装饰器只是语法糖。如前所示，装饰器可以像常规的可调用对象那样调用
# ，其参数是另一个函数。

def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print("running target()")

if __name__ == "__main__":
    target()        # 执行装饰器返回的函数
    print(target)   # target 是 inner 对象的引用
    pass

# running inner()
# <function deco.<locals>.inner at 0x101609378>
