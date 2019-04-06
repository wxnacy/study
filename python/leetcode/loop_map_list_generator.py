#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: for while generator list_comprehension map 对比速度

from collections.abc import Iterable, Iterator, Generator

def loop_generator(n):
    res = (abs(i) for i in range(n))
    return res

def loop_list_compre(n):
    res = [abs(i) for i in range(n)]
    return res

def loop_map(n):
    return map(abs, range(n))

import utils

if __name__ == "__main__":
    count = 1000
    n = 1000
    gen_res = loop_generator(10)
    map_res = loop_map(10)
    list_res = loop_list_compre(10)
    #  print(isinstance(loop_list_compre(10), Iterable))
    #  print(isinstance(map_res, Generator))
    #  print(isinstance(map_res, Iterator))
    #  print(isinstance(list_res, Iterator))
    utils.print_func_run_time(count, loop_list_compre, n = n)
    utils.print_func_run_time(count, loop_map, n = n)
    utils.print_func_run_time(count, loop_generator, n = n)

# loop_list_compre     run 1000 times used 0.08865494900237536s
# loop_map             run 1000 times used 0.0007684140000492334s
# loop_generator       run 1000 times used 0.0009459810025873594s
