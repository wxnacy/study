#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 使用多线程下载

from concurrent import futures

from flags import download_one, main

MAX_WORKERS = 20

def download_many(suffixs):
    workers = min(MAX_WORKERS, len(suffixs))
    with futures.ThreadPoolExecutor(workers) as executor:
        to_do = []
        for s in suffixs:
            future = executor.submit(download_one, s)
            to_do.append(future)
            print(f'Scheduled {s}: {future}')

        results = []
        for f in futures.as_completed(to_do):
            res = f.result()
            results.append(res)
            print(f'{f} result {res}')


    return len(results)


if __name__ == "__main__":
    main(download_many)




