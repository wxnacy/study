#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from multiprocessing import Pool
import time,os,random

#定义一个函数
def download(i):
    print('%d--ID号为:%d的进程开始执行'%(i,os.getpid()))
    t_start=time.time()
    #time.sleep(2)
    time.sleep(random.random()*10)

    t_stop=time.time()
    print('%d--ID:%d执行完毕，耗时：%f秒'%(i,os.getpid(),t_stop-t_start))

if __name__=='__main__':
    po=Pool(3)#定义一个进程池，最大进程数量
    for i in range(10):
        #假设有10个文件要下载
        #同步，自加阻塞
        #po.apply(func=download,args=(i,))
        #将请求放进进程池中执行,属于阻塞式请求，一个进程执行完毕后才会执行第二个进程
        # 不能体现同时处理三个三个请求
        #也就是不能体现并发
        #每次循环将会用空闲出来的子进程去调用任务---异步
        po.apply_async(func=download,args=(i,))
        #异步体现并发，三个进程都在执行任务，其中一个执行完毕后，下一个补上继续执行
    print('----start-----')

    #调用join之前，先调用close函数，否则会出错。
    po.close()#关闭进程池，关闭后就不再接受新的请求，即开始执行任务。
    po.join()## join函数等待所有子进程结束，才会执行主进程之后的代码
    print('-----end------')
