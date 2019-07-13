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


from datetime import datetime
from datetime import date
from functools import singledispatch

class CustomEncoder(json.JSONEncoder):
    def default(self, x):
        try:
            return encode(x)
        except TypeError:
            return super().default(self, x)

@singledispatch
def encode(x):
    raise TypeError('Unencode type')

@encode.register(datetime)
def _(x):
    return int(x.timestamp())

@encode.register(date)
def _(x):
    return x.isoformat()

print(json.dumps(dict(dt = datetime.now(), d = date.today()), cls=CustomEncoder))
# {"dt": 1562940781, "d": "2019-07-12"}

class CustomDecoder(json.JSONDecoder):
    def default(self, x):
        if isinstance(x, str):
            return int(x.timestamp())
        return super.default(self, x)

def dumps_encoder():
    '''
    {
        "id": 1,
        "name": "wxnacy"
    }
    '''
    USER_DATA = dict(
        id = 1, name = 'wxnacy', ts = datetime.now()
    )
    print(json.dumps(USER_DATA, cls=CustomEncoder))
    #  print(json.dumps(USER_DATA))

if __name__ == "__main__":
    #  dumps()
    #  dumps_indent()
    #  dumps_skipkeys()
    dumps_encoder()
    print(CustomEncoder().encode(datetime.now()))


