#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:


import numpy

#生成正态分布
x = numpy.round(numpy.random.normal(1.75, 0.2, 5000),2)
y = numpy.round(numpy.random.normal(100, 10, 5000), 2)
#使成为二维数组
z = numpy.column_stack((x, y))
print(z)
#输出身高均值（输出体重均值只需将0改为1）
print(numpy.mean(z[:, 0]))
#输出身高中位数
print(numpy.median(z[:, 0]))
#输出两组数据相关系数
print(numpy.corrcoef(z[:, 0 ], z[:, 1]))
#输出身高标准差
print(numpy.std(z[:, 0]))
