#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import numpy as np

a = np.array([2, 3, 4])
print(a)
# [2 3 4]

# 指定数据 dtype
a = np.array([2, 3, 4], dtype = np.int)
print(a.dtype)          # int64
a = np.array([2, 3, 4], dtype = np.int32)
print(a.dtype)          # int32
a = np.array([2, 3, 4], dtype = np.float)
print(a.dtype)          # float64
a = np.array([2, 3, 4], dtype = np.float32)
print(a.dtype)          # float32

# 创建特定数据
a = np.array([[1, 2, 3], [4, 5, 6]])        # 矩阵
print(a)
# [[1 2 3]
#  [4 5 6]]

a = np.zeros((2, 3))                        # 数据全部为 0，2 行 3 列
print(a)
# [[0. 0. 0.]
#  [0. 0. 0.]]

a = np.ones((2, 3))                         # 数据全部为 1，2 行 3 列
print(a)
# [[1. 1. 1.]
#  [1. 1. 1.]]

a = np.empty((2, 3))
print(a)

a = np.arange(10,20,2)                      # 10-19 的数据，2步长
print(a)
# [10 12 14 16 18]

a = np.arange(12).reshape((3,4))            # 3行4列，0到11
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

a = np.linspace(1,10,20)    # 开始端1，结束端10，且分割成20个数据，生成线段
print(a)
# [ 1.          1.47368421  1.94736842  2.42105263  2.89473684  3.36842105
#   3.84210526  4.31578947  4.78947368  5.26315789  5.73684211  6.21052632
#   6.68421053  7.15789474  7.63157895  8.10526316  8.57894737  9.05263158
#   9.52631579 10.        ]

a = np.linspace(1,10,20).reshape((5,4))     # 更改shape
print(a)
# [[ 1.          1.47368421  1.94736842  2.42105263]
#  [ 2.89473684  3.36842105  3.84210526  4.31578947]
#  [ 4.78947368  5.26315789  5.73684211  6.21052632]
#  [ 6.68421053  7.15789474  7.63157895  8.10526316]
#  [ 8.57894737  9.05263158  9.52631579 10.        ]]
