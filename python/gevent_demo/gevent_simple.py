#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import gevent

import os
import threading
import time

def print_func_progress():
    print('[{}] Greenlet {} Process {} - Thread {}'.format(
        time.time(), gevent.getcurrent(), os.getpid(), threading.current_thread().ident))

def foo():
    print_func_progress()
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')

def bar():
    print_func_progress()
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')


if __name__ == "__main__":


    gevent.joinall([
        gevent.spawn(foo),
        gevent.spawn(bar),
    ])

# [1553694796.1719072] Greenlet <Greenlet at 0x10e9a4930: foo> Process 2022 - Thread 4683818432
# Running in foo
# [1553694796.171974] Greenlet <Greenlet at 0x10e9a4a60: bar> Process 2022 - Thread 4683818432
# Explicit context to bar
# Explicit context switch to foo again
# Implicit context switch back to bar
