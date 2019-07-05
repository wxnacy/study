#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from quick_sort import quick_sort
from quick_sort import quick_sort_3partition
from bubble_sort import bubble_sort
from heap_sort import heap_sort
from merge_sort import merge_sort
from merge_sort import merge_sort_fastest
from counting_sort import counting_sort
from insertion_sort import insertion_sort
from bucket_sort import bucket_sort
from bucket_sort import bucket_sort_array
from selection_sort import selection_sort
from radix_sort import radix_sort
import utils
import os
import sys

if __name__ == "__main__":
    length = 1
    n = 7000
    #  print()
    #  for name, func in sys.modules.items():
        #  print(name, func)
        #  #  if '_sort' in name:
            #  #  print(name, func.)

    #  funcs = (bubble_sort, selection_sort, insertion_sort, quick_sort,
        #  quick_sort_3partition, heap_sort, merge_sort, merge_sort_fastest,
        #  counting_sort, bucket_sort, bucket_sort_array, radix_sort)

    times = []
    #  for f in funcs:
        #  n, t = utils.print_func_run_time(length, f, utils.generate_random(int(n))[0])
        #  #  times.append((n, t))
    #  #  times.sort(key = lambda x: x[1])
    #  #  for n, t in times:
        #  #  print(n, t)
    

    times.append(utils.print_func_run_time(length, bubble_sort,
        utils.generate_random(n)[0]))
    times.append(utils.print_func_run_time(length, selection_sort,
        utils.generate_random(n)[0]))
    times.append(utils.print_func_run_time(length, insertion_sort,
        utils.generate_random(n)[0]))
    times.append(utils.print_func_run_time(length, quick_sort,
        utils.generate_random(n)[0]))
    times.append(utils.print_func_run_time(length, quick_sort_3partition,
        utils.generate_random(n)[0]))
    times.append(utils.print_func_run_time(length, heap_sort,
        utils.generate_random(n)[0]))
    times.append(utils.print_func_run_time(length, merge_sort,
        utils.generate_random(n)[0]))
    times.append(utils.print_func_run_time(length, merge_sort_fastest,
        utils.generate_random(n)[0]))
    times.append(utils.print_func_run_time(length, counting_sort,
        utils.generate_random(n)[0]))
    times.append(utils.print_func_run_time(length, bucket_sort,
        utils.generate_random(n)[0]))
    times.append(utils.print_func_run_time(length, bucket_sort_array,
        utils.generate_random(n)[0]))
    times.append(utils.print_func_run_time(length, radix_sort,
        utils.generate_random(n)[0]))


    print('正在排序')
    times.sort(key = lambda x: x[1])
    for n, t in times:
        print(n.ljust(25), t)
