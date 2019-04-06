#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 复制文件的几种方式

import shutil
import shlex
import subprocess
import os

SOURCE_FILE = '/tmp/test.sh'

def copy_file():
    '''
    shutil.copyfile() 只复制文件内容，不复制权限等信息

    -rwxr-xr-x  1 wxnacy  wheel     90 Apr  6 19:05 test.sh
    -rw-r--r--  1 wxnacy  wheel     90 Apr  6 19:08 test_copy_file.sh
    '''
    shutil.copyfile(SOURCE_FILE, '/tmp/test_copy_file.sh')

def copy():
    '''
    shutil.copy() 将内容和权限全部复制

    -rwxr-xr-x  1 wxnacy  wheel     90 Apr  6 19:05 test.sh
    -rwxr-xr-x  1 wxnacy  wheel     90 Apr  6 19:09 test_copy.sh
    '''
    shutil.copy(SOURCE_FILE, '/tmp/test_copy.sh')

def popen():
    '''
    subprocess.Popen() 直接调用 shell 命令，是最灵活的

    Windows 平台需要使用 `copy source_file target_file`

    -rwxr-xr-x  1 wxnacy  wheel     90 Apr  6 19:05 test.sh
    -rwxr-xr-x  1 wxnacy  wheel     90 Apr  6 19:23 test_popen.sh
    '''
    cmds = shlex.split("cp {} /tmp/test_popen.sh".format(SOURCE_FILE))
    p = subprocess.Popen(cmds)
    p.wait()

if __name__ == "__main__":
    # 创建源文件
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

