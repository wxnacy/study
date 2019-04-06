#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 在 Mac 系统中使用剪切板

import subprocess

def set_clipboard(data: str):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(data.encode("utf-8"))
    p.stdin.close()
    p.communicate()

def get_from_clipboard():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    p.wait()
    byte_data = p.stdout.read()
    p.stdout.close()
    return byte_data.decode('utf-8')

if __name__ == "__main__":
    set_clipboard('我爱你中国')
    print(get_from_clipboard())

