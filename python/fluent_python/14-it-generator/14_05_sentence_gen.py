#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 使用生成器实现可迭代对象

import re
import reprlib
from collections.abc import Iterable
from collections.abc import Iterator
from collections.abc import Generator

RE_WORD = re.compile('\w+')

class Sentence():
    def __init__(self, text):
        self.text = text
        # .findall 函数返回的结果，因此直接返回指定索引位上的单词。
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        for w in self.words:
            yield w

    def __repr__(self):
        '''
        reprlib.repr 这个实用函数用于生成大型数据结构的简略字符串
        默认情况下，reprlib.repr 函数生成的字符串最多有 30 个字 符。
        '''
        return f'Sentence({reprlib.repr(self.text)})'


if __name__ == "__main__":
    s = Sentence("My name is wxnacy. The website is 'https://wxnacy.com'")
    print(isinstance(s, Iterable))      # True
    print(isinstance(iter(s), Iterator))      # True
    print(isinstance(iter(s), Generator))      # True
    print(s)        # Sentence("My name is w...//wxnacy.com'")
    print(list(s))  # ['My', 'name', 'is', 'wxnacy', 'The', 'website', 'is',
                    # 'https', 'wxnacy', 'com']
    for w in s:
        print(w)
