#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 测试 gunicorn 配置
# 运行：gunicorn -c config.py flask_app:app

from flask import Flask
import time
import os


app = Flask(__name__)

@app.route('/out5seconds')
def out5seconds():
    print(os.getpid())
    time.sleep(5)
    return 'Hello World'

@app.route('/out11seconds')
def out11seconds():
    print(os.getpid())
    time.sleep(11)
    return 'Hello World'

@app.route('/hello')
def hello():
    print(os.getpid())
    app.logger.info('Hello World')
    return 'Hello World'

if __name__ == "__main__":
    app.run()

