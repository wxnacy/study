# Python 协程库 gevent

> [gevent](https://github.com/gevent/gevent) 是一个基于 libev 的并发库。它为各种并发和网络相关的任务提供了整洁的API。

Python 中多线程的性能极差，替代它的另一种“并发”方式是协程。

Python 版本中协程一直在不断的进化
- `yeild` python2.x
- `asynico + yield from` python3.4
- `asynico + await` python3.5

而这个过程中，一直可以拿来就用的三方库就是 gevent

在gevent中用到的主要模式是Greenlet, 它是以C扩展模块形式接入Python的轻量级协程。 Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。

> 在任何时刻，只有一个协程在运行。

换句话说，协程并不会切换线程或进程（所以性能会比多线程高很多），而是在 IO 阻塞时，可以切换到其他的 Greenlet，等到适当时机再切换回来，这样减少阻塞浪费的时间，使其看起来像是在并发。所以协程可以解决 IO 密集的性能问题，而 CPU 密集则无能为力。

## 异步执行

首先安装 gevent

```bash
$ pip install gevent
```

我们来模拟程序的阻塞，使用 `gevent.sleep(0)` 主动让程序交出执行权。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import gevent

import os
import threading
import time

def print_func_progress():
    print('[{}] Greenlet {} Process {} - Thread {}'.format(
        time.time(), gevent.getcurrent(), os.getpid(), threading.current_thread().ident))

def foo():
    print_func_progress()
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')

def bar():
    print_func_progress()
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')

if __name__ == "__main__":
    gevent.joinall([
        gevent.spawn(foo),
        gevent.spawn(bar),
    ])

# [1553694796.1719072] Greenlet <Greenlet at 0x10e9a4930: foo> Process 2022 - Thread 4683818432
# Running in foo
# [1553694796.171974] Greenlet <Greenlet at 0x10e9a4a60: bar> Process 2022 - Thread 4683818432
# Explicit context to bar
# Explicit context switch to foo again
# Implicit context switch back to bar
```

从打印结果中，可以看到无论是进程 `Process`，还是线程 `Thread`，整个过程都是没有变化的，所以再次确定了协程是单线程运行的。并且在运行过程中，协程在两个方法间切换，以减少阻塞浪费的时间。

## 隐形交出执行权

当我们的程序受限于网络的 IO 阻塞时，gevent 才能真正发挥实力，它提供了方法，可以隐形的交出上下文执行权，这样我们可以在不改变程序结构的情况下来实现协程。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import requests

import timeit

def print_func_run_time(count, func, **kw):
    b = timeit.default_timer()
    for i in range(count):
        func(**kw)
    print(func.__name__, 'run {} times used {}s'.format(count,
        timeit.default_timer() -b ))

def fetch(pid):
    print('pid {} begin request url', pid)
    response = requests.get('http://baidu.com')
    print('pid {} get response status {}', pid, response.status_code)

def synchronous():
    for i in range(0,5):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(0,5):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Synchronous:')
print_func_run_time(1, synchronous)

print('Asynchronous:')
print_func_run_time(1, asynchronous)

# Synchronous:
# pid {} begin request url 0
# pid {} get response status {} 0 200
# pid {} begin request url 1
# pid {} get response status {} 1 200
# pid {} begin request url 2
# pid {} get response status {} 2 200
# pid {} begin request url 3
# pid {} get response status {} 3 200
# pid {} begin request url 4
# pid {} get response status {} 4 200
# synchronous run 1 times used 0.13507633499102667s
# Asynchronous:
# pid {} begin request url 0
# pid {} begin request url 1
# pid {} begin request url 2
# pid {} begin request url 3
# pid {} begin request url 4
# pid {} get response status {} 0 200
# pid {} get response status {} 4 200
# pid {} get response status {} 3 200
# pid {} get response status {} 1 200
# pid {} get response status {} 2 200
# asynchronous run 1 times used 0.03902721201302484s
```

从结果中我们可以看到，使用 gevent 执行的程序，性能比顺序执行好了很多倍，而在功能函数中，我们也并没有主动交出执行权，这一些都归功于猴子补丁 `gevent.monkey`

## 猴子补丁

猴子补丁(monkey patching) 得以让 gevent 变得更加强大。上面的代码中我们用到了 `gevent.monkey.patch_socket()`，它修改了 Python 的 socket 标准库。

```python
>>> import socket
>>> socket.socket
<class 'socket.socket'>
>>> from gevent import monkey
>>> monkey.patch_socket()
>>> socket.socket
<class 'gevent._socket3.socket'>
```

Python的运行环境允许我们在运行时修改大部分的对象，包括模块，类甚至函数。所以猴子补丁的实现原理很简单，比如：

```python
>>> import json
>>> json.__name__
'json'
>>> def patch_json():
...     json.__name__ = 'wjson'
...
>>> patch_json()
>>> json.__name__
'wjson'
```

在这种情况下，gevent能够 修改标准库里面大部分的阻塞式系统调用，包括socket、ssl、threading和 select等模块，而变为协作式运行。通常情况下我们只需要调用 `gevent.monkey.patch_all()`，它可以修改所有可以兼容的模块

`patch_all()` 方法语法如下

```python
def patch_all(socket=True, dns=True, time=True, select=True, thread=True, os=True, ssl=True,
              httplib=False, # Deprecated, to be removed.
              subprocess=True, sys=False, aggressive=True, Event=True,
              builtins=True, signal=True,
              queue=True,
              **kwargs):
```

如果不想修改某个模块，直接传参即可，比如

```python
patch_all(socket=False)
```

或者在该方法之后导入，让原始模块覆盖掉 monkey 的修改即可

```python
>>> monkey.patch_all()
>>> import select
>>> select.select
<function select at 0x100e40f28>
```

## gevent without code

猴子补丁如此厉害，好像可以不用主动写 gevent 代码就可以实现。其实真的可以不用任何 gevent 代码，就可以让程序实现协程，只需要使用可以调用 gevent 的容器来启动程序即可。

我们来使用 gunicorn 来启动一个 Flask 程序。

如果你不了解 gunicorn，可以看我的这篇文章[使用 gunicorn 启动你的项目](/2017/08/15/python-2017-08-15-gunicorn-run/)

安装模块

```bash
$ pip install gunicorn
$ pip install flask
```

编辑文件

```bash
$ touch gevent_without_code.py
$ vim gevent_without_code.py
```

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import time
import socket
from flask import Flask
app = Flask(__name__)

print(socket.socket)

@app.route('/for')
def get():
    time.sleep(4)
    return "for"

@app.route('/bar')
def get2():
    return "bar"
```

不使用 gevent 启动

```bash
$ gunicorn gevent_without_code:app

[2019-03-27 23:06:53 +0800] [53872] [INFO] Starting gunicorn 19.7.1
[2019-03-27 23:06:53 +0800] [53872] [INFO] Listening at: http://127.0.0.1:8000 (53872)
[2019-03-27 23:06:53 +0800] [53872] [INFO] Using worker: sync
[2019-03-27 23:06:53 +0800] [53932] [INFO] Booting worker with pid: 53932
<class 'socket.socket'>
[2019-03-27 23:06:56 +0800] [53872] [INFO] Handling signal: winch
```

gunicorn 默认启动一个 8000 端口的 web 程序，我们有两个接口 `/for` 强制睡眠 4 秒钟，`/bar` 直接返回结果

这时候我们先访问 `/for` 在访问 `/bar` 会发生阻塞

![gevent1](https://wxnacy-img.oss-cn-beijing.aliyuncs.com/blog/gevent1.gif)

`/bar` 需要等待 `/for` 返回结果后才能执行，这显然不是一个健康的程序。我们试试使用 gevent。

`<ctrl> + c` 停掉程序，重新启动

```bash
$ gunicorn gevent_without_code:app -k gevent
[2019-03-27 23:16:41 +0800] [63766] [INFO] Starting gunicorn 19.7.1
[2019-03-27 23:16:41 +0800] [63766] [INFO] Listening at: http://127.0.0.1:8000 (63766)
[2019-03-27 23:16:41 +0800] [63766] [INFO] Using worker: gevent
[2019-03-27 23:16:41 +0800] [63826] [INFO] Booting worker with pid: 63826
<class 'gevent._socket3.socket'>
```

再次访问两个接口，效果非常明显

![gevent2](https://wxnacy-img.oss-cn-beijing.aliyuncs.com/blog/gevent2.gif)

当 `/for` 阻塞时，gevent 直接跳过执行 `/bar`，等阻塞过后，在继续执行 `/for`。

这里我们一句 gevent 代码都没写，那它是什么实现的呢？

如果你留意刚才的启动日志，会发现我们代码有句 `print(socket.socket)`，在使用 gevent 前后是有不同的。

```bash
...
<class 'socket.socket'>
...

...
<class 'gevent._socket3.socket'>
...
```

就像我们上面讲到的那样，gevent 在这里隐形的调用了 `gevent.monkey.patch_all()` 方法，使得相关的程序都自动变成了协程可调用的状态。

不管你代码写的怎么样，用 gevent 来启动你的项目吧，一定会让你觉得物有所值。

- [gevent 源码](https://github.com/gevent/gevent)
- [gevent 程序员指南](http://hhkbp2.github.io/gevent-tutorial/)
