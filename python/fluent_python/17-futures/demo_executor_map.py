#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import time
from concurrent import futures

def display(*args):
    print(time.strftime('[%H:%M:%S]'), end=' ')
    print(*args)

def loiter(n):
    prefix = '\t' * n
    display(f'{prefix}loiter({n}): doing nothing for {n}s...')
    time.sleep(n)
    display(f'{prefix}loiter({n}): done')

def main():
    display('Script starting')
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(5))
    display(f'Results {results}')
    display('Waiting for results')
    for i, result in enumerate(results):
        display(f'Result {i}: {result}')

if __name__ == "__main__":
    t0 = time.clock()
    main()
    t1 = time.clock()
    display(f'Total time: {t1 - t0}')
