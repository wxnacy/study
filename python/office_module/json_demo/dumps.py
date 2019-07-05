#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: json.dumps() 函数可以将字典对象序列化为字符串

import json

USER_DATA = dict(
    id = 1, name = 'wxnacy'
)

def dumps():
    ''' {"id": 1, "name": "wxnacy"} '''
    print(json.dumps(USER_DATA))

def dumps_indent():
    '''
    {
        "id": 1,
        "name": "wxnacy"
    }
    '''
    print(json.dumps(USER_DATA, indent=4))

def dumps_skipkeys():
    '''
    {
        "id": 1,
        "name": "wxnacy"
    }
    '''
    print(json.dumps(USER_DATA, skipkeys=True))

def dumps_skipkeys():
    '''
    {
        "id": 1,
        "name": "wxnacy"
    }
    '''
    print(json.dumps(USER_DATA, skipkeys=True))

if __name__ == "__main__":
    dumps()
    dumps_indent()
    dumps_skipkeys()

