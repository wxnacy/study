#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])  # 将数组转化为矩阵
print(arr)
print('ndim\t', arr.ndim)               # 维度
print('shape\t', arr.shape)             # 行数和列数
print('size\t', arr.size)               # 元素个数

# [[1 2 3]
#  [4 5 6]]
# ndim	 2
# shape	 (2, 3)
# size	 6
