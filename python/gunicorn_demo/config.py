#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 常用 gunicorn 配置

import multiprocessing

#  workers=multiprocessing.cpu_count() * 2 + 1
# 配置进程数
workers=1
timeout=6                       # 请求的超时秒数，仅在 sync 模式下生效
# 使用 gevent 来做协程
worker_class='gevent'
bind='127.0.0.1:8765'
# 热更新
reload = True
access_log_format = '%(h)s %(t)s %(r)s %(m)s %(s)s %(T)s %(D)s %(B)s %(U)s %(q)s'
accesslog='/tmp/gunicorn.log'


