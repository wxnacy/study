#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 使用元类

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print("new instance")
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SingClass(metaclass=Singleton):
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
