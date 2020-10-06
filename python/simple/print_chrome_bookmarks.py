#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 打印 Chrome 书签列表

import os
import json

# 书签地址
FILEPATH = os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/Bookmarks')

def get_bookmarks():
    '''获取书签 json 数据'''
    with open(FILEPATH, 'r') as f:
        return json.loads(f.read())

def _print(items):
    '''打印列表'''
    for item in items:
        type = item['type']
        name = item['name']
        if type == 'url':
            print(name, item['url'])
        else:
            # 遇到文件夹循环调用
            _print(item['children'])

def main():
    data = get_bookmarks()
    items = data['roots']['bookmark_bar']['children']
    _print(items)

if __name__ == "__main__":
    main()


