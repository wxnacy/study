#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:  参数化装饰器

registry = set()

def register(active=True):

    def decorate(func):
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate

@register()
def f1():
    print('running f1')

@register(active=False)
def f2():
    print('running f2')

if __name__ == "__main__":
    f1()
    f2()
    print(registry)     # {<function f1 at 0x109fb6158>}
