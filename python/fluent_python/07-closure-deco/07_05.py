#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 变量作用域

b = 3

def f1(a):
    print(a)
    print(b) # UnboundLocalError: local variable 'b' referenced before assignment
    b = 9

def f2():
    b = 9
    print(b)

def f3():
    global b
    print(b)
    b = 9


if __name__ == "__main__":
    #  f1(1)
    f2()        # 9
    print(b)    # 3
    f3()        # 3
    print(b)    # 9


