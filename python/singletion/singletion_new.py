#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 使用 __new__ 方法

class Singletion():
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            print("new instance")
            cls._instance = super().__new__(cls, *args, **kw)
        return cls._instance

class SingClass(Singletion):
    def get(self):
        print("get class")

c = SingClass()
c.get()

c1 = SingClass()
c1.get()

# 输出结果：
# new instance
# get class
# get class
