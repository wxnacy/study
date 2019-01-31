#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 装饰器模式

def singletion(cls):
    instance = {}
    def get_instance(*args, **kw):
        if cls not in instance:
            print("new instance")
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return get_instance

@singletion
class User():
    def get(self):
        print("get class")

u = User()
u.get()
u1 = User()
u1.get()

# 输出结果：
# new instance
# get class
# get class

