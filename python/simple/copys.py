#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 复制文件的几种方式
'''
直接实现
shutil.copyfile()
shutil.copy()

调用 shell 命令，因为现在 subprocess 是用来代替其他执行 shell 命令的模块，所以
不在介绍其他模块，比如 os
subprocess.Popen()
'''

import shutil
import shlex
import subprocess
import os

SOURCE_FILE = '/tmp/test.sh'
TARGET_DIR = '/tmp/tmp'

def copy_file():
    '''
    shutil.copyfile() 只复制文件内容，不复制权限等信息，目标文件不能是目录，否
    则报错

    -rwxr-xr-x  1 wxnacy  wheel     90 Apr  6 19:05 test.sh
    -rw-r--r--  1 wxnacy  wheel     90 Apr  6 19:08 test_copy_file.sh
    '''
    target_file = '/tmp/test_copy_file.sh'
    shutil.copyfile(SOURCE_FILE, target_file)
    #  shutil.copyfile(target_file, TARGET_DIR)
# Traceback (most recent call last):
#   File "/Users/wxnacy/PycharmProjects/study/python/simple/copys.py", line 56, in <module>
#     copy_file()
#   File "/Users/wxnacy/PycharmProjects/study/python/simple/copys.py", line 22, in copy_file
#     shutil.copyfile(target_file, '/tmp/tmp')
#   File "/Users/wxnacy/.pyenv/versions/3.6.0/Python.framework/Versions/3.6/lib/python3.6/shutil.py", line 115, in copyfile
#     with open(dst, 'wb') as fdst:
# IsADirectoryError: [Errno 21] Is a directory: '/tmp/tmp'

def copy():
    '''
    shutil.copy() 将内容和权限全部复制，目标文件可以是目录

    -rwxr-xr-x  1 wxnacy  wheel     90 Apr  6 19:05 test.sh
    -rwxr-xr-x  1 wxnacy  wheel     90 Apr  6 19:09 test_copy.sh
    '''
    target_file = '/tmp/test_copy.sh'
    shutil.copy(SOURCE_FILE, target_file)
    shutil.copy(target_file, TARGET_DIR)


def popen():
    '''
    subprocess.Popen() 直接调用 shell 命令，命令行能实现的它都能实现，是最灵活的

    Windows 平台需要使用 `copy source_file target_file`

    -rwxr-xr-x  1 wxnacy  wheel     90 Apr  6 19:05 test.sh
    -rwxr-xr-x  1 wxnacy  wheel     90 Apr  6 19:23 test_popen.sh
    '''
    cmds = shlex.split("cp {} /tmp/test_popen.sh".format(SOURCE_FILE))
    p = subprocess.Popen(cmds)
    p.wait()

if __name__ == "__main__":
    # 创建源文件
    flag = os.path.exists(TARGET_DIR)
    if not flag:
        os.mkdir(TARGET_DIR)
    with open(SOURCE_FILE, 'w') as f:
        f.writelines(['#!/usr/bin/env bash', 'echo "Hello World"'])
        f.flush()
        f.close()
    # 赋予执行权限
    p = subprocess.Popen(shlex.split("chmod +x {}".format(SOURCE_FILE)))
    p.wait()
    copy_file()
    copy()
    popen()

