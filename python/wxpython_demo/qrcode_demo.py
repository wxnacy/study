#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import os
import wx

try:
    import qrcode
except ImportError:
    qrcode = None

try:
    import PyQRNative
except ImportError:
    PyQRNative = None

########################################################################
class QRPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        self.photo_max_size = 240
        sp = wx.StandardPaths.Get()
        self.defaultLocation = sp.GetDocumentsDir()

        img = wx.EmptyImage(240,240)
        self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.BitmapFromImage(img))

        qrDataLbl = wx.StaticText(self, label="Text to turn into QR Code:")
        self.qrDataTxt = wx.TextCtrl(self, value="http://www.mousevspython.com", size=(200,-1))
        instructions = "Name QR image file"
        instructLbl = wx.StaticText(self, label=instructions)
        self.qrPhotoTxt = wx.TextCtrl(self, size=(200,-1))
        browseBtn = wx.Button(self, label='Change Save Location')
        browseBtn.Bind(wx.EVT_BUTTON, self.onBrowse)
        defLbl = "Default save location: " + self.defaultLocation
        self.defaultLocationLbl = wx.StaticText(self, label=defLbl)

        qrcodeBtn = wx.Button(self, label="Create QR with qrcode")
        qrcodeBtn.Bind(wx.EVT_BUTTON, self.onUseQrcode)
        pyQRNativeBtn = wx.Button(self, label="Create QR with PyQRNative")
        pyQRNativeBtn.Bind(wx.EVT_BUTTON, self.onUsePyQR)

        # Create sizer
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        qrDataSizer = wx.BoxSizer(wx.HORIZONTAL)
        locationSizer = wx.BoxSizer(wx.HORIZONTAL)
        qrBtnSizer = wx.BoxSizer(wx.VERTICAL)

        qrDataSizer.Add(qrDataLbl, 0, wx.ALL, 5)
        qrDataSizer.Add(self.qrDataTxt, 1, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(wx.StaticLine(self, wx.ID_ANY),
                           0, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(qrDataSizer, 0, wx.EXPAND)
        self.mainSizer.Add(self.imageCtrl, 0, wx.ALL, 5)
        locationSizer.Add(instructLbl, 0, wx.ALL, 5)
        locationSizer.Add(self.qrPhotoTxt, 0, wx.ALL, 5)
        locationSizer.Add(browseBtn, 0, wx.ALL, 5)
        self.mainSizer.Add(locationSizer, 0, wx.ALL, 5)
        self.mainSizer.Add(self.defaultLocationLbl, 0, wx.ALL, 5)

        qrBtnSizer.Add(qrcodeBtn, 0, wx.ALL, 5)
        qrBtnSizer.Add(pyQRNativeBtn, 0, wx.ALL, 5)
        self.mainSizer.Add(qrBtnSizer, 0, wx.ALL|wx.CENTER, 10)

        self.SetSizer(self.mainSizer)
        self.Layout()

    #----------------------------------------------------------------------
    def onBrowse(self, event):
        """"""
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.defaultLocation = path
            self.defaultLocationLbl.SetLabel("Save location: %s" % path)
        dlg.Destroy()

    #----------------------------------------------------------------------
    def onUseQrcode(self, event):
        """
        https://github.com/lincolnloop/python-qrcode
        """
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(self.qrDataTxt.GetValue())
        qr.make(fit=True)
        x = qr.make_image()

        qr_file = os.path.join(self.defaultLocation, self.qrPhotoTxt.GetValue() + ".jpg")
        img_file = open(qr_file, 'wb')
        x.save(img_file, 'JPEG')
        img_file.close()
        self.showQRCode(qr_file)

    #----------------------------------------------------------------------
    def onUsePyQR(self, event):
        """
        http://code.google.com/p/pyqrnative/
        """
        qr = PyQRNative.QRCode(20, PyQRNative.QRErrorCorrectLevel.L)
        qr.addData(self.qrDataTxt.GetValue())
        qr.make()
        im = qr.makeImage()

        qr_file = os.path.join(self.defaultLocation, self.qrPhotoTxt.GetValue() + ".jpg")
        img_file = open(qr_file, 'wb')
        im.save(img_file, 'JPEG')
        img_file.close()
        self.showQRCode(qr_file)

    #----------------------------------------------------------------------
    def showQRCode(self, filepath):
        """"""
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        # scale the image, preserving the aspect ratio
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            NewW = self.photo_max_size
            NewH = self.photo_max_size * H / W
        else:
            NewH = self.photo_max_size
            NewW = self.photo_max_size * W / H
        img = img.Scale(NewW,NewH)

        self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
        self.Refresh()


########################################################################
class QRFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="QR Code Viewer", size=(550,500))
        panel = QRPanel(self)

if __name__ == "__main__":
    app = wx.App(False)
    frame = QRFrame()
    frame.Show()
    app.MainLoop()
