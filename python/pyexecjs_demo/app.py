#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import os
import execjs
import json

os.environ["EXECJS_RUNTIME"] = "Node"
os.environ["NODE_PATH"] = os.getcwd()+"/node_modules"

f = open(os.getcwd() + "/index.js")
text = f.read()
parser = execjs.compile(text)

if __name__ == "__main__":
    obj = parser.call("test", 'function add(first, second) { return first + second;    }')
    print(obj)
