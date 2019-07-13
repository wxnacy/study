#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import re
RE_CHINESE = re.compile(u"[\u4e00-\u9fa5]+")  # 正则查找中文

def charlen(s):
    '''
    Return the str's char len
    '''
    ch_results = RE_CHINESE.findall(s)
    return len(s) + len(''.join(ch_results))

def charepr(s, width=30):
    realen = charlen(s)
    if realen <= width:
        return s
    substr = ''
    max_str_len = 0
    for a in s:
        if charlen(substr) + charlen(a) + 3 > width:
            break
        substr += a
        max_str_len = charlen(substr)
    return substr + '.' * (width - charlen(substr))

def charljust(s, width, fullchar=' '):
    print(width, charlen(s), len(s))
    w = width - (charlen(s) - len(s))
    return s.ljust(w, fullchar)

import time
data = [
    dict(id = 12345, name='wxnacy', time=time.time()),
    dict(id = 12345, name='拖延心理学-简·博克', time=time.time()),
    dict(id = 12345, name='拖延心理学-简', time=time.time()),
]

for d in data:
    d['name'] = charljust(charepr(d['name'], 8), 8, '*')
    #  d['name'] = name.ljust(w)
    line = f'{d["id"]}\t{d["name"]}\t{d["time"]}'
    print(line)
