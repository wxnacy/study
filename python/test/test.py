#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

class User():
    id = 1
    def get(self):
        return self.id

if __name__ == "__main__":
    import sys
    print(sys.modules)
    print(dir(sys.modules[__name__]))
    print(dir(sys.modules[User.__class__.__module__]))
    print(sys.main)
