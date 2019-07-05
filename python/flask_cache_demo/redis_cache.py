#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 使用 redis 做缓存
# http://www.pythondoc.com/flask-cache/index.html
'''
RedisCache – redis

相关配置

    CACHE_DEFAULT_TIMEOUT
    CACHE_KEY_PREFIX
    CACHE_REDIS_HOST
    CACHE_REDIS_PORT
    CACHE_REDIS_PASSWORD
    CACHE_REDIS_DB
    CACHE_ARGS
    CACHE_OPTIONS
    CACHE_REDIS_URL

不配置 CACHE_KEY_PREFIX 和 key_prefix 时，默认 key 为 flask_cache_view/{route}

'''

from flask import Flask
from flask import jsonify
from flask import request
from flask_caching import Cache
import random

app = Flask(__name__)
cache = Cache(app, config={
    "CACHE_TYPE": "redis",
    "CACHE_REDIS_URL": "redis://localhost:6379/0",  # redis 地址
    "CACHE_DEFAULT_TIMEOUT": 10,                    # 全局过期时间
    # key 前缀，key 为 redis_cache_view/{route}
    "CACHE_KEY_PREFIX": "redis_cache_",
})

@app.route('/redis1')
@cache.cached()
def redis1():
    '''
    key=redis_cache_view//redis1
    '''
    return jsonify({"num": random.randint(1, 100)})

@app.route('/redis2')
@cache.cached(timeout = 20, key_prefix='customize')
def redis2():
    '''
    自定义过期时间 20
    key=redis_cache_customize
    '''
    return jsonify({"num": random.randint(1, 100)})

def make_cache_key():
    path = request.path
    key = str(hash(request.args))
    return f'{path}-{key}'


@app.route('/redis3')
@cache.cached(timeout = 20, key_prefix=make_cache_key)
def redis3():
    '''
    自定义 key
    key=redis_cache_/redis3-133156838395276
    '''
    return jsonify({"num": random.randint(1, 100)})

@app.route('/redis4')
def redis4():
    '''
    自定义 key
    key=redis_cache_/redis3-133156838395276
    '''
    return jsonify(redis4_data())

@cache.cached(timeout = 60)
def redis4_data():
    return {"num": random.randint(1, 100)}


if __name__ == "__main__":
    app.run(debug=True)

