#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 装饰器的一个关键特性是，它们在被装饰的函数定义之后立即运行。
# 这通常是在导入时（即Python加载模块时）


registry = []

def register(func):
    print(f'running register({func})')
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    print('running main()')
    print(f'registry -> {registry}')
    f1()
    f2()
    f3()

if __name__ == "__main__":
    main()

# running register(<function f1 at 0x105485048>)
# running register(<function f2 at 0x1054850d0>)
# running main()
# registry -> [<function f1 at 0x105cb3048>, <function f2 at 0x105cb30d0>]
# running f1()
# running f2()
# running f3()
