#!/usr/bin/env python
# ! -*- coding:utf-8 -*-
"""聚合api"""
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

import requests


class Juhe():
    KEY = 'bc7ca9c13a7a5e078764d43a99a5b384'  # '434f9ee2dd5c7d6646ae0fec4a80f08c'  #
    KEY2 = '434f9ee2dd5c7d6646ae0fec4a80f08c'
    KEYS = ['bc7ca9c13a7a5e078764d43a99a5b384']

    def __init__(self, key):
        self.key = key

    @classmethod
    def get_new_joke_img(cls, page, per_page):
        return requests.get(
            url='http://japi.juhe.cn/joke/img/text.from',
            params={
                "page": page,
                "pagesize": per_page,
                "key": cls.KEY
            }
        ).json()


    def get_img_by_time(self, time, sort, page, per_page):
        return requests.get(
            url='http://japi.juhe.cn/joke/img/list.from',
            params={
                "time": time,
                "sort": sort,
                "page": page,
                "pagesize": per_page,
                "key": self.key
            }
        ).json()


if __name__ == '__main__':
    pass
