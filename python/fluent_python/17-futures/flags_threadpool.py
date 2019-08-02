#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 使用多线程下载

from concurrent.futures import ThreadPoolExecutor

from flags import download_one, main

MAX_WORKERS = 20

def download_many(suffixs):
    workers = min(MAX_WORKERS, len(suffixs))
    with ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, suffixs)
    return len(list(res))


if __name__ == "__main__":
    main(download_many)




