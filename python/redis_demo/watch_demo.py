#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 使用 redis 的 watch 特性来实现简单的防止商品超卖的 demo

import redis
from threading import Thread

# 创建连接池
pool = redis.ConnectionPool(host = '127.0.0.1', port=6379, db=0)
# 初始化 redis
r = redis.Redis(connection_pool = pool)

KEY="count"     # 库存 key

class BaseThread(Thread):
    '''封装异步多线程工具'''
    def __init__(self, func, *args, **kwargs):
        super(BaseThread, self).__init__()
        self.func = func
        self._args = args
        self._kwargs = kwargs

    def run(self):
        self.func(*self._args, **self._kwargs)

def sell(i):
    '''
    售卖方法
    param: i 用户
    '''
    with r.pipeline() as pipe:              # 初始化 pipe
        while 1:
            try:
                pipe.watch(KEY)             # 监听库存
                c = int(pipe.get(KEY))      # 查看当前库存
                if c > 0:                   # 有库存则售卖
                    pipe.multi()            # 开始事务
                    c -= 1
                    pipe.set(KEY, c)        # 减少库存
                    pipe.execute()          # 执行事务
                    # 抢购成功并结束
                    print('用户 {} 抢购成功，商品剩余 {}'.format(i, c))
                    break
                else:
                    # 库存卖完，抢购结束
                    print('用户 {} 抢购停止，商品卖完'.format(i))
                    break
            except Exception as e:
                # 抢购失败，重试
                print('用户 {} 抢购失败，重试一次'.format(i))
                continue
            finally:
                # 重置 pipe，准备下次抢购
                pipe.reset()

if __name__ == "__main__":
    r.set(KEY, 10)                  # 初始化 10 个库存
    for i in range(15):             # 共 15 个人开始抢购
        t = BaseThread(sell, i)
        t.start()                   # 使用异步线程，模拟并发

#  python watch_demo.py
#  用户 0 抢购成功，商品剩余 9
#  用户 1 抢购成功，商品剩余 8
#  用户 2 抢购失败，重试一次
#  用户 3 抢购成功，商品剩余 7
#  用户 5 抢购失败，重试一次
#  用户 4 抢购失败，重试一次
#  用户 2 抢购失败，重试一次
#  用户 6 抢购失败，重试一次
#  用户 7 抢购失败，重试一次
#  用户 9 抢购失败，重试一次
#  用户 8 抢购成功，商品剩余 6
#  用户 10 抢购成功，商品剩余 5
#  用户 5 抢购成功，商品剩余 4
#  用户 12 抢购失败，重试一次
#  用户 6 抢购失败，重试一次
#  用户 13 抢购成功，商品剩余 3
#  用户 11 抢购失败，重试一次
#  用户 14 抢购失败，重试一次
#  用户 2 抢购失败，重试一次
#  用户 4 抢购失败，重试一次
#  用户 9 抢购成功，商品剩余 2
#  用户 7 抢购失败，重试一次
#  用户 12 抢购成功，商品剩余 1
#  用户 2 抢购停止，商品卖完
#  用户 6 抢购失败，重试一次
#  用户 14 抢购失败，重试一次
#  用户 4 抢购停止，商品卖完
#  用户 11 抢购成功，商品剩余 0
#  用户 7 抢购停止，商品卖完
#  用户 6 抢购停止，商品卖完
#  用户 14 抢购停止，商品卖完
