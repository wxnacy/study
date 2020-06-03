#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import re
from collections import namedtuple

RE_INT = re.compile(r'<int:\w*>')
RE_STRING = re.compile(r'<string:\w*>')
RE_TYPES = ((RE_INT, r'(\d+)'), (RE_STRING, r'(\w+)'))

#  url = '/tmdapi/v3/screen/WXIW24/shop/566'
#  rule = '/tmdapi/v3/screen/<string:code>/shop/<int:shop_id>'
url = '/tmdapi/v3/test'
rule = '/tmdapi/v3/test'
re_com = r'(<int:\w*>|<string:\w*>)'
RE_FIELD = re.compile(re_com)
fields = []

field_params = re.findall(RE_FIELD, rule)
print(field_params)
for fp in field_params:
    fields.append(fp.split(":")[1][:-1])
print(fields)

rule_reg = rule
for ren, rev in RE_TYPES:
    print(rule_reg)
    rule_reg = ren.sub(rev, rule_reg)

print(rule_reg)
url_reg = re.compile(rule_reg)
path_values = re.findall(url_reg, url)
print(path_values, fields)
if path_values and fields:
    Value = namedtuple('Value', fields)
    val = Value(*path_values[0])
    print(val)
    print(dir(val))
    print(val._asdict())
    val = dict(val._asdict())
    print(val.get('code'), type(val))
    


res = re.findall(re.compile('^/test$'), '/test')
print(res)



