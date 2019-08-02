#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 使用 asyncio 和 aiohttp 实现异步下载

import asyncio

import aiohttp

from flags import BASE_URL, save_flag, show, main

@asyncio.coroutine
def get_flag(suffix):
    url = BASE_URL.format(suffix)
    resp = yield from aiohttp.request('GET', url)
    image = yield from resp.read()
    return image

@asyncio.coroutine
def download_one(suffix):
    image = yield from get_flag(suffix)
    show(suffix)
    save_flag(image, suffix)
    return suffix

def download_many(suffixs):
    loop = asyncio.get_event_loop()
    to_do = [download_one(o) for o in suffixs]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)

if __name__ == "__main__":
    main(download_many)

