#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import json
import requests
import os
import subprocess
import bisect

download_path = "/Users/wxnacy/Downloads/girls/"
album_file = "/Users/wxnacy/PycharmProjects/study/python/scrapy_demo/first/album_neidi.json"


def download_album(item):
    girl_id = item['girl_id']
    album_id = item['id']

    for i in range(1000):
        path = '{}{}.{}.{}.jpg'.format(download_path,
            item['girl_name'], item['name'], i
        )
        path = path.replace(" ", "-")
        if os.path.exists(path):
            continue
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

        try:
            res = requests.head(url)
            if res.status_code != 200:
                return
        except Exception as e:
            print(e)
            continue


        #  f = open(path, 'w+')
        #  f.write(res.content)
        #  f.close()
        #  os.system('wget {} -O {}'.format(url, path))

        try:
            subprocess.check_output(['wget', url, '-O', path])
        except Exception as e:
            print(e)
            continue



import bisect

def binary_search(nums, n):
    i = bisect.bisect_left(nums, n)
    if i >= len(nums):
        return -1
    else:
        if nums[i] == n:
            return i
        else:
            return -1

import unittest

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def do(self, func):
        '''todo'''
        self.assertEqual(1, 1)
        pass

    def test_bs(self):
        a = [1, 4, 4, 5, 6]
        self.assertEqual(binary_search(a, 3), -1)
        self.assertEqual(binary_search(a, 8), -1)
        self.assertEqual(binary_search(a, 4), 1)


if __name__ == "__main__":
    unittest.main()
