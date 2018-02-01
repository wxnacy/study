#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import os
import execjs
import json

os.environ["EXECJS_RUNTIME"] = "Node"
os.environ["NODE_PATH"] = os.getcwd()+"/node_modules"

parser = execjs.compile("""
var uglifyjs = require('uglify-js');

const test = (text) => {
    return uglifyjs.minify(text);
}
                    """)

if __name__ == "__main__":
    obj = parser.call("test", 'function add(first, second) { return first + second;    }')
    print(obj)
