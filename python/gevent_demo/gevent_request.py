#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import requests

import timeit

def print_func_run_time(count, func, **kw):
    b = timeit.default_timer()
    for i in range(count):
        func(**kw)
    print(func.__name__, 'run {} times used {}s'.format(count,
        timeit.default_timer() -b ))

def fetch(pid):
    print('pid {} begin request url', pid)
    response = requests.get('http://baidu.com')
    print('pid {} get response status {}', pid, response.status_code)

def synchronous():
    for i in range(0,5):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(0,5):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Synchronous:')
#  synchronous()
print_func_run_time(1, synchronous)

print('Asynchronous:')
#  asynchronous()
print_func_run_time(1, asynchronous)

# Synchronous:
# pid {} begin request url 0
# pid {} get response status {} 0 200
# pid {} begin request url 1
# pid {} get response status {} 1 200
# pid {} begin request url 2
# pid {} get response status {} 2 200
# pid {} begin request url 3
# pid {} get response status {} 3 200
# pid {} begin request url 4
# pid {} get response status {} 4 200
# synchronous run 1 times used 0.13507633499102667s
# Asynchronous:
# pid {} begin request url 0
# pid {} begin request url 1
# pid {} begin request url 2
# pid {} begin request url 3
# pid {} begin request url 4
# pid {} get response status {} 0 200
# pid {} get response status {} 4 200
# pid {} get response status {} 3 200
# pid {} get response status {} 1 200
# pid {} get response status {} 2 200
# asynchronous run 1 times used 0.03902721201302484s
