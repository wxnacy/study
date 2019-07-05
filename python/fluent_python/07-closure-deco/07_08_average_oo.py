#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

class Averager():
    def __init__(self, *args, **kwargs):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        return sum(self.series) / len(self.series)

if __name__ == "__main__":
    ave = Averager()
    print(ave(10))  # 10.0
    print(ave(11))  # 10.5
    print(ave(12))  # 11.0
