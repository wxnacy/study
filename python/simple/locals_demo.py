#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:


#  name = 'wxnacy'
#  age = 1

def func(**kw):
    name = 'wxnacy'
    print(locals())

if __name__ == "__main__":
    #  print(locals())
    #  name = 'wxnacy'
    #  print(locals())
    func(url = 'https://wxnacy.com')
