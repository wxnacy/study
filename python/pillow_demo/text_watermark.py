#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 添加文字水印

from overlay import get_image
from overlay import image2bytes

from PIL import ImageDraw
from PIL import ImageFont

def add_watermark(image, text, position, color=(0, 0, 0), font=None):
    '''给图片对象添加文字水印'''
    draw=ImageDraw.Draw(image)
    draw.text(position,text,color, font=font)
    image.show()
    return image2bytes(image)

if __name__ == "__main__":

    image = get_image('https://wxnacy.com/images/rss.png')
    font=ImageFont.truetype('PingFang.ttc',40)
    add_watermark(image, 'This is wxnacy\'s website', (70, 300), (0, 255, 255),
            font)
