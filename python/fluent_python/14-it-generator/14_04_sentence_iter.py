#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 使用迭代器实现可迭代对象

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

    def __iter__(self):
        return SentenceIterator(self.words)

    def __repr__(self):
        '''
        reprlib.repr 这个实用函数用于生成大型数据结构的简略字符串
        默认情况下，reprlib.repr 函数生成的字符串最多有 30 个字 符。
        '''
        return f'Sentence({reprlib.repr(self.text)})'

class SentenceIterator():
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


if __name__ == "__main__":
    s = Sentence("My name is wxnacy. The website is 'https://wxnacy.com'")
    print(isinstance(s, Iterable))      # True
    print(isinstance(iter(s), Iterator))      # True
    print(s)        # Sentence("My name is w...//wxnacy.com'")
    print(list(s))  # ['My', 'name', 'is', 'wxnacy', 'The', 'website', 'is',
                    # 'https', 'wxnacy', 'com']
    for w in s:
        print(w)
