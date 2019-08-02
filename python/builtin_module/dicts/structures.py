#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: dict 的几种构造方式

a = {"one": 1, "two": 2}

b = dict(one = 1, two = 2)

c = dict(zip(["one", "two"], [1, 2]))

d = dict([("one", 1), ("two", 2)])

e = dict(a)

# 字典推导
f = {k: v for k, v in [("one", 1), ("two", 2)]}

print(a == b == c == d == e == f)      # True


