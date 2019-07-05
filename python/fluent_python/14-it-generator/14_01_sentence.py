#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 实现可迭代对象
# 按照《设计模式：可复用面向对象软件的基础》一书讲解迭代器设计模式的实现方式
# 但并不符合 Python 的开发模式

import re
import reprlib
from collections.abc import Iterable
from collections.abc import Iterator

RE_WORD = re.compile('\w+')

class Sentence():
    def __init__(self, text):
        self.text = text
        # .findall 函数返回的结果，因此直接返回指定索引位上的单词。
        self.words = RE_WORD.findall(text)
        self.size = len(self.words)

    def __getitem__(self, index):
        '''
        可以直接使用索引获取单词的魔法函数

        如果没有实现 __iter__ 方法，但是实现了 __getitem__ 方法，
        Python 会创建一个迭代器，尝试按顺序（从索引 0 开始）获取元素。
        '''
        return self.words[index]

    def __len__(self):
        return self.size

    def __repr__(self):
        '''
        reprlib.repr 这个实用函数用于生成大型数据结构的简略字符串
        默认情况下，reprlib.repr 函数生成的字符串最多有 30 个字 符。
        '''
        return f'Sentence({reprlib.repr(self.text)})'



if __name__ == "__main__":
    s = Sentence("My name is wxnacy. The website is 'https://wxnacy.com'")
    print(isinstance(s, Iterable))  # False
    print(isinstance(iter(s), Iterator))  # True
    print(s)        # Sentence("My name is w...//wxnacy.com'")
    print(list(s))  # ['My', 'name', 'is', 'wxnacy', 'The', 'website', 'is',
                    # 'https', 'wxnacy', 'com']
    print(len(s))   # 10
    print(s[0])     # My
    for w in s:
        print(w)
