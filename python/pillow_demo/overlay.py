#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 图片叠加

import io

from PIL import Image
import requests


def get_image(path):
    '''通过地址获取 image 对象'''
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

def overlay(big_path, small_path, width, height, small_thumbnail=()):
    '''图片叠加'''
    big_image = get_image(big_path)
    small_image = get_image(small_path)
    if small_thumbnail:
        small_image.thumbnail(small_thumbnail)
    big_image.paste(small_image,(width, height))
    big_image.show()    # 显示图片
    #  big_image.save('/Users/wxnacy/Downloads/pillow_overlay.png')  # 保存
    # 或者返回图片的二进制
    return image2bytes(big_image)


if __name__ == "__main__":
    overlay('https://wxnacy.com/images/rss.png',
            'https://wxnacy.com/images/mp.jpg', 157, 45)

