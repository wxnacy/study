#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 使用文件系统来存储缓存值
# http://www.pythondoc.com/flask-cache/index.html
'''
FileSystemCache – filesystem
使用文件系统来存储缓存值

CACHE_DEFAULT_TIMEOUT
CACHE_DIR
CACHE_THRESHOLD
CACHE_ARGS
CACHE_OPTIONS
'''

from flask import Flask
from flask import jsonify
from flask_caching import Cache
import random

app = Flask(__name__)
cache = Cache(app, config={
    "CACHE_TYPE": "filesystem",
    "CACHE_DIR": "/Users/wxnacy/Downloads/cache"
})

@app.route('/filesystem')
@cache.cached(timeout=10)
def filesystem():
    return jsonify({"num": random.randint(1, 100)})

if __name__ == "__main__":
    app.run(debug=True)

