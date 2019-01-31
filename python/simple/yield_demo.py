#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

def test():

    for i in range(5):
        yield i

if __name__ == "__main__":
    for i in test():
        print(i)

    print(test())

    for i in test():
        print(i)


