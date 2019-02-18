#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import json
import requests
import os
import subprocess


def download_album(item):
    girl_id = item['girl_id']
    album_id = item['id']

    for i in range(1000):
        url = ''
        if i == 0:
            url = 'https://img.onvshen.com:85/gallery/{}/{}/s/0.jpg'.format(
                    girl_id, album_id
                    )
        else:
            url = 'https://img.onvshen.com:85/gallery/{}/{}/s/{:0>3d}.jpg'.format(
                    girl_id, album_id, i
                    )
        print(url)

        res = requests.get(url)
        if res.status_code != 200:
            return

        path = '/Users/wxnacy/Downloads/girls/{}.{}.{}.jpg'.format(
            item['girl_name'], item['name'], i
                )

        #  f = open(path, 'w+')
        #  f.write(res.content)
        #  f.close()
        #  os.system('wget {} -O {}'.format(url, path))
        subprocess.check_output(['wget', url, '-O', path])


if __name__ == "__main__":
    with open('/Users/wxnacy/PycharmProjects/study/python/scrapy_demo/first/album_neidi.json') as f :
        text = f.read()
        data = json.loads(text)
        for i in data:
            print(i)
            download_album(i)


