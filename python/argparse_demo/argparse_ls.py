#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 模拟 ls

import argparse
import os

def init_args():
    '''初始化参数'''
    parser = argparse.ArgumentParser(description='List files')
    parser.add_argument('files', help='Specify some files or directorys',
        nargs='?')
    parser.add_argument('-a', help='Whether to show hidden files',
            action="store_true")
    return parser.parse_args()

def list_files(files=None, is_all=False):
    '''列出目标目录的文件'''
    if not files:
        files = ['./']
    print(files)

    for f in files:
        filenames = os.listdir(f)
        for filename in filenames:
            is_hide = filename.startswith('.')
            if not is_hide or is_all:
                print(filename, end='\t')
    print()

if __name__ == "__main__":
    args = init_args()
    list_files(args.files, args.a)



