#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:
'''
语法： print('\033[显示方式;字体色;背景色m文本\033[0m')
三种设置都可以忽略不写，都不写则为默认输出

# 前景 背景 颜色
# ---------------------------------------
# 30  40  黑色
# 31  41  红色
# 32  42  绿色
# 33  43  黄色
# 34  44  蓝色
# 35  45  紫红色
# 36  46  青蓝色
# 37  47  白色
#
# 显示方式
# -------------------------
#  0  终端默认设置
#  1  高亮显示
#  4  使用下划线
#  5  闪烁
#  7  反白显示
#  8  不可见

'''

from enum import Enum

class Color(Enum):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37

def print_color(text: str, fg: Color = Color.BLACK.value):
    print(f'\033[{fg}m{text}\033[0m')

# 打印红色文字
print_color('Hello World', fg = Color.RED.value)

