#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from uiautomator import device as d
from uiautomator import Device
from uiautomator import Adb
from uiautomator import AutomatorDevice, Selector

# = Device('8Q40-01B3-11509423')
d = Device('emulator-5554')
#  d = Device('10.2.0.41:5555')
#  d = Device('372b2388d8b260a8')
#  d = Device(adb_server_host='10.2.0.41', adb_server_port=5555)
#  d = AutomatorDevice()


for k, v in d.info.items():
    print(k, v)
#  d.press.back()
d.press.home()
d.press.up()
d.press.right()
d.press.enter()
#  d.press.home()
#  d.press.menu()
#  d.press.center()

#  adb = Adb()
#  res = adb.devices()
#  print(res)
#  print(adb.adb())
