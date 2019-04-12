#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 打印不换行进度条
# 预览 https://raw.githubusercontent.com/wxnacy/image/master/blog/python_progress.gif

import time


def get_progress(progress, total):
    '''获取进度条'''
    progress_ratio = progress / total
    progress_len = 20
    progress_num = int(progress_ratio * 20)
    pro_text = '[{:-<20s}] {:.2f}% {} / {}'.format(
        '=' * progress_num, progress_ratio * 100, progress, total)
    return pro_text

def print_progress(total):
    '''模拟打印进度条'''
    progress = 0
    step = 30
    while progress < total:
        time.sleep(1)
        b = progress
        e = b + step
        progress += step
        end = '\r'
        if progress >= total:
            end = '\n'
            progress = total
        print(get_progress(progress, total), end = end)

if __name__ == "__main__":
    print_progress(100)


