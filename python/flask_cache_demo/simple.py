#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 使用本地Python字典缓存。这不是真正的线程安全。
# http://www.pythondoc.com/flask-cache/index.html
'''
SimpleCache – simple
使用本地Python字典缓存。这不是真正的线程安全。

相关配置

CACHE_DEFAULT_TIMEOUT
CACHE_THRESHOLD
CACHE_ARGS
CACHE_OPTIONS
'''

from flask import Flask
from flask import jsonify
from flask_caching import Cache
import random

app = Flask(__name__)
cache = Cache(app, config={"CACHE_TYPE": "simple"})

@app.route('/simple')
@cache.cached(timeout=10)
def simple():
    return jsonify({"num": random.randint(1, 100)})

if __name__ == "__main__":
    app.run(debug=True)

