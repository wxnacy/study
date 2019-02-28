#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import random



def rand_int_arr(length):

    arr = []
    for i in range(length):
        r = random.randrange(1000)
        arr.append(r)
    return arr

if __name__ == "__main__":
    arr = rand_int_arr(10)
    print(list(arr))
