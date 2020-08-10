#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import aiohttp
import asyncio

async def get(n):
    print('begin')
    await asyncio.sleep(1)
    print('end')
    #  async with aiohttp.ClientSession() as client:
        #  print('begin')
        #  resp = await client.get(f'http://httpbin.org/delay/{n}')
        #  result = await resp.json()
        #  print
    #  print(result)

#  asyncio.run(get(1))
import time
b = time.time()
loop = asyncio.get_event_loop()
tasks = []
for i in range(10):
    tasks.append(get(i))
#  tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
print(asyncio.current_task(loop))
loop.close()
print(time.time() - b)
