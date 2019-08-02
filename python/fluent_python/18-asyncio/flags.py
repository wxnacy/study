#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 顺发下载多个图片

import os
import sys
import time
import timeit

import requests

SUFFIX = '1 2 3 4 5'.split()

BASE_URL = 'https://wxnacy.com/images/gzjzz{}.png'

DOWNLOAD_DIR = '/Users/wxnacy/Downloads/flags'

def get_flag(suffix):
    url = BASE_URL.format(suffix)
    res = requests.get(url)
    return res.content

def save_flag(img, suffix):
    path = os.path.join(DOWNLOAD_DIR, suffix)
    with open(path, 'wb') as f:
        f.write(img)

def show(text):
    print(text, end=' ')
    sys.stdout.flush()

def download_one(suffix):
    image = get_flag(suffix)
    show(suffix)
    save_flag(image, f'{time.time()}-{suffix}.gif')

def download_many(suffixs):
    for s in suffixs:
        download_one(s)
    return len(suffixs)

def main(download_many):
    t0 = timeit.default_timer()
    count = download_many(SUFFIX)
    t1 = timeit.default_timer()
    print(f'\n{count} images downloaded in {(t1-t0):.2f}s')

if __name__ == "__main__":
    if not os.path.exists(DOWNLOAD_DIR):
        os.mkdir(DOWNLOAD_DIR)
    main(download_many)



