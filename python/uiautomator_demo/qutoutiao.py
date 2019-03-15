#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

#  from uiautomator import device as d
from uiautomator import Device
import time

d = Device('emulator-5554')

for k, v in d.info.items():
    print(k, v)

def one_time():
    print('等待新闻加载')
    time.sleep(5)
    for i in range(3):
        if d(text='查看全文，奖励更多'):
            d(text='查看全文，奖励更多').click()
        d.swipe(360, 1100, 360, 400, steps = 10)
        print('下滑屏幕')
        print('模拟看新闻')
        time.sleep(5)
    print('返回首页')
    d.press.back()

def run():
    d.screen.on()
    print('点亮屏幕')
    for i in range(10000):
        d.click(360, 640)
        print('点击新闻')
        one_time()
        time.sleep(2)
        print('下拉新闻列表')
        d.swipe(360, 1100, 360, 800, steps = 10)
        time.sleep(2)
        #  d.click(360, 640)


if __name__ == "__main__":
    run()
    #  one_time()

