#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 

import asyncio

import requests

url = 'https://baidu.com'

async def async_get():
    #  res = requests.get(url)
    await asyncio.sleep(1)
    #  return res.status_code
    return 1

def async_gets():
    loop = asyncio.get_event_loop()
    loop.run_until_complete([async_get() for o in range(3)])
    loop.close()

def get():
    res = requests.get(url)
    return res.status_code

def gets():
    for i in range(3):
        print(get())


if __name__ == "__main__":
    #  gets()
    async_gets()
