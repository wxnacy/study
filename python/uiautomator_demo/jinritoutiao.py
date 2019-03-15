#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from uiautomator import device as d
import time

for k, v in d.info.items():
    print(k, v)

d.screen.on()
#  d.swipe(360, 1100, 360, 100, steps = 80)
d.swipe(360, 1100, 360, 100)

#  total = 5 * 60 * 60
#  interval = 30
#  inprogress = 0

#  def fanye(inprogress):
    #  d.screen.on()
    #  d.click(700, 1200)
    #  time.sleep(interval)
    #  inprogress += interval
    #  print(inprogress)
    #  print('本次已经观看 {} 秒'.format(inprogress))
    #  return inprogress

#  if __name__ == "__main__":
    #  inprogress = 0
    #  while inprogress < total:
        #  inprogress = fanye(inprogress)
    
