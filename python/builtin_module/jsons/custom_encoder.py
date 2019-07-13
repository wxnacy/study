#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 自定义 JSONEncoder

import json
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


if __name__ == "__main__":
    print(json.dumps(dict(dt = datetime.now(), d = date.today()), cls=CustomEncoder))
