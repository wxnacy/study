#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import os
import multiprocessing
import requests

# worker function
def worker(sign, lock):
    lock.acquire()
    print(sign, os.getpid())
    res = requests.get("https://wxnacy.com")
    print(res)
    lock.release()

# Main
print('Main:',os.getpid())

# Multi-process

#  lock = multiprocessing.Lock()
#  for i in range(5):
    #  process = multiprocessing.Process(target=worker,args=('process',lock))
    #  process.start()
    #  process.join()

#  for process in record:
    #  process.join()

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    record = []
    for i in range(5):
        process = multiprocessing.Process(target=worker,args=(f'process {i}',lock))
        process.start()
        record.append(process)

    for process in record:
        process.join()
