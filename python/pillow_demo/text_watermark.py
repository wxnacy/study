#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from overlay import get_image
from overlay import image2bytes

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#  draw=ImageDraw.Draw(image)
#  font=ImageFont.truetype('PingFang.ttc',40)
#  draw.text((70,300),'This is wxnacy\'s website',(0,255,255), font=font)
#  image.show()

def add_watermark(image, text, position, color=(0, 0, 0), font=None):
    draw=ImageDraw.Draw(image)
    draw.text(position,text,color, font=font)
    image.show()
    return image2bytes(image)


if __name__ == "__main__":

    image = get_image('https://wxnacy.com/images/rss.png')
    font=ImageFont.truetype('PingFang.ttc',40)
    add_watermark(image, 'This is wxnacy\'s website', (70, 300), (0, 255, 255),
            font)
