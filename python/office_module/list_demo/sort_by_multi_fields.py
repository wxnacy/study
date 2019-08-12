#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 列表使用多个属性进行排序
# 例子：用户列表先按照年龄正序排序，如果年龄相同，按照创建 id 倒序排序

from datetime import datetime
from functools import cmp_to_key

import time
import random

def make_users():
    items = []
    for i in range(10):
        items.append(dict(id=i, age=random.randint(1, 5)))
    return items

def sortd(arr, *fields):
    def _sort(a, b):
        for f in fields:
            name = f
            sort_by = 'asc'
            if ' ' in f:
                name = f.split()[0]
                sort_by = f.split()[1]

            if a[name] < b[name]:
                return -1 if sort_by  == 'asc' else 1
            elif a[name] > b[name]:
                return 1 if sort_by  == 'asc' else -1

        return 0

    arr.sort(key=cmp_to_key(_sort))
    return arr



if __name__ == "__main__":

    users = make_users()
    print(users)
    sortd(users, 'age', 'id desc')
    # or
    #  sortd(users, 'age asc', 'id desc')
    print(users)

# [{'id': 0, 'age': 3}, {'id': 1, 'age': 2}, {'id': 2, 'age': 5}, {'id': 3, 'age': 1}, {'id': 4, 'age': 4}, {'id': 5, 'age': 1}, {'id': 6, 'age': 3}, {'id': 7, 'age': 5}, {'id': 8, 'age': 3}, {'id': 9, 'age': 5}]
# [{'id': 5, 'age': 1}, {'id': 3, 'age': 1}, {'id': 1, 'age': 2}, {'id': 8, 'age': 3}, {'id': 6, 'age': 3}, {'id': 0, 'age': 3}, {'id': 4, 'age': 4}, {'id': 9, 'age': 5}, {'id': 7, 'age': 5}, {'id': 2, 'age': 5}]
