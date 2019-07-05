#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

class ArithmeticProgression():

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


if __name__ == "__main__":
    ap = ArithmeticProgression(0, 2, 7)
    print(list(ap)) # [0, 2, 4, 6]
    for a in ap:
        print(a)
# 0
# 2
# 4
# 6
