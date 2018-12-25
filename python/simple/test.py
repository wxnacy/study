#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

count = 0

a = [1, 2, 3]

def fmt(i):
    #  global count
    count += i

[fmt(o) for o in a]
print(count)
