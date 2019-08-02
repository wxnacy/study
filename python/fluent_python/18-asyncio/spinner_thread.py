#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import threading
import itertools
import time
import sys

class Signal:
    go = True

def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = f'{char}  {msg}'
        write(status)
        flush()
        write('\x08' * len(status))
        time.sleep(.1)
        if not signal.go:
            break
    write(' ' * len(status) + '\x08' * len(status))

def slow_function():
    time.sleep(3)
    return 42

def supervisor():
    signal = Signal()
    spinner = threading.Thread(target = spin, args=('thinking!', signal))
    print('spinner object', spinner)
    spinner.start()
    result = slow_function()
    signal.go = False
    spinner.join()
    return result


if __name__ == "__main__":
    #  sys.stdout.write('test')
    #  sys.stdout.flush()
    #  sys.stdout.write(' \x08')
    result = supervisor()
    print('Answer', result)
