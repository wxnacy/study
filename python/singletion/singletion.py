#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: import 需要的部分

class User():
    def __new__(cls, *args, **kw):
        print("new instance")
        return super().__new__(cls, *args, **kw)

    def get(self):
        print("get class")


u = User()
u.get()
