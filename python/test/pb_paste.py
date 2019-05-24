#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from PIL import ImageGrab
from PIL import Image
import io

img = ImageGrab.grabclipboard()
img_bytes = io.BytesIO()
print(img_bytes)
if isinstance(img, Image.Image):
    #  img.save('test.png', 'png')
    img.save(img_bytes, 'png')
    print(img_bytes.getvalue())

print(img_bytes.getvalue())

