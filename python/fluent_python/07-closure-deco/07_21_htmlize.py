#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:
# Python3.4新增的functools.singledispatch装饰器可以把整体方案拆分成多个模块，
# 甚至可以为你无法修改的类提供专门的函数。使用 @singledispatch 装饰的普通函数会变成泛函数（genericfunction）：根据第一个参数的类型，以不同方式执行相同操作的一组函数。
# 这才称得上是单分派。如果根据多个参数选择专门的函数，那就是多分派了。

from functools import singledispatch
from collections import abc
import html
import numbers

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return f'<p>{content}</p>'

@htmlize.register(numbers.Integral)
def _(n):
    return f'<pre>{n} (0x{n:x})</pre>'

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return f'<ul>\n<li>{inner}</li>\n</ul>'

if __name__ == "__main__":
    print(htmlize('wxnacy'))
    print(htmlize('wxnacy\nwebsite'))
    print(htmlize(4))
    print(htmlize([1, 2, 3]))
