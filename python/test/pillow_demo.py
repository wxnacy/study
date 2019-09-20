#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import io

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import requests

def get_image(path):
    '''通过网络或本地地址获取 image 对象'''

    image = None
    if path.startswith('http'):
        res = requests.get(path)
        image = Image.open(io.BytesIO(res.content))
    else:
        image = Image.open(path)
    return image

def image2bytes(image):
    '''图片转二进制'''
    img_bytes = io.BytesIO()
    image.save(img_bytes, image.format)
    return img_bytes.getvalue()

def overlay(big_path, small_path):
    big_image = get_image(big_path)
    small_image = get_image(small_path)
    #  small_image.thumbnail((200, 200))
    big_image.paste(small_image, (157, 45))
    big_image.show()
    #  big_image.save('/Users/wxnacy/Downloads/pillow_demo/overlay.png')
    return image2bytes(big_image)

def watermark(image_path, text):
    '''添加文字水印'''
    image = get_image(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('PingFang.ttc', 40)
    draw.text((70, 300), text, (0, 0, 0), font=font)
    #  image.show()
    return image2bytes(image)



if __name__ == "__main__":
    #  image = get_image('https://wxnacy.com/images/rss.png')
    #  image.show()
    #  bytes_data = overlay('https://wxnacy.com/images/rss.png',
            #  'https://wxnacy.com/images/mp.jpg')
    #  with open('/Users/wxnacy/Downloads/pillow_demo/test.png', 'wb') as f:
        #  f.write(bytes_data)

    watermark('https://wxnacy.com/images/rss.png', 'This is wxnacy\'s website')
