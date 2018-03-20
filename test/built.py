#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

class User():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name


if __name__ == "__main__":
    a = User(1, 'wxnacy')
    b = User(2, 'ning')
    c = [a, b]
    print(a in c)

