#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import numpy as np

a = np.array([10, 20, 30, 40])          # [10 20 30 40]
b = np.arange(4)                        # [0 1 2 3]
print(a - b)                            # [10 19 28 37]
print(a + b)                            # [10 21 32 43]
print(a * b)                            # [  0  20  60 120 ]
print(b ** 3)                           # [ 0  1  8 27 ]    3 次方
print(np.sin(a))
# [-0.54402111  0.91294525 -0.98803162 0.74511316] 属性函数
print(b < 3)                            # [ True  True  True False ] 逻辑判断
print(b == 1)                           # [False  True False False]

a = np.arange(4).reshape((2, 2))
# [[0 1]
#  [2 3]]
b = np.arange(4, 8).reshape((2, 2))
# [[4 5]
#  [6 7]]
print(np.dot(a, b))
# [[ 6  7]
#  [26 31]]
print(b.dot(a))
# [[10 19]
#  [14 27]]

#  print(np.arange(6).reshape((2, 3)).dot(np.arange(6).reshape((2, 3))))

# Traceback (most recent call last):
#   File "/Users/wxnacy/PycharmProjects/study/python/numpy_demo/operation.py", line 31, in <module>
#     print(np.arange(6).reshape((2, 3)).dot(np.arange(6).reshape((2, 3))))
# ValueError: shapes (2,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)

a = np.random.random((2, 3))
print(a)
# [[0.79601161 0.848222   0.58032891]
#  [0.5456669  0.27207342 0.62963501]]
print(np.sum(a))                        # 3.671937844780624
print(np.min(a))                        # 0.27207342302472903
print(np.max(a))                        # 0.8482220009868361
