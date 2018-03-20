#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import wx

class PostFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        panel = MainPanel(self)

class MainPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)

if __name__ == "__main__":
    app = wx.App()
    frame = PostFrame(None, title = 'PostKid')
    frame.Show()
    app.MainLoop()
