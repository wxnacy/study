#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 不写 gevent 代码也可以实现协程

import time
import socket
from flask import Flask
app = Flask(__name__)

print(socket.socket)

@app.route('/for')
def get():
    time.sleep(4)
    return "for"

@app.route('/bar')
def get2():
    return "bar"

# pip install flask
# pip install gunicorn
# 不使用协程启动，先访问 /for 在访问 /bar 会发生阻塞
# gunicorn gevent_without_code:app
# 使用协程启动，先访问 /for 在访问 /bar 会自动跳过阻塞先执行 /bar 再回去执行 /for
# gunicorn gevent_without_code:app -k gevent
