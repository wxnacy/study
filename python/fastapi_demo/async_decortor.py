#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from functools import wraps
from functools import update_wrapper

from inspect import isfunction

CACHE = {}
import asyncio

def cached(timeout=600, key_prefix=None):
    """
    缓存
    """
    def _wrapper(func):
        @wraps(func)
        async def _wrapped(*args, **kwargs):
            cache_key = func.__name__

            cache_data = CACHE.get(cache_key)
            if cache_data:
                return cache_data
            res = await func(*args, **kwargs)
            if timeout > 0:
                CACHE[cache_key] = res
            else:
                CACHE[cache_key] = res
            return res

        return _wrapped
    return _wrapper

from datetime import datetime

@cached()
async def test():
    print(CACHE)
    res = datetime.now().isoformat()
    print(res)
    return res

asyncio.run(test())
asyncio.run(test())
asyncio.run(test())
