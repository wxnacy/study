#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import scrapy

class WxnacySpider(scrapy.Spider):
    name = 'wxnacy'
    start_urls = ['https://wxnacy.com']

    def parse(self, response):
        #  print(response.css('a'))
        print(dir(response))
        #  print(response.url)
        #  print(response.text)
        t = 'test'
        for a in response.css('header'):
            yield a
