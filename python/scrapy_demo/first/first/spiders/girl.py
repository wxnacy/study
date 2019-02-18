#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import scrapy

class GirlSpider(scrapy.Spider):
    name = "girl"
    allowed_domains = ["nvshens.com"]
    start_urls = [
        "https://m.nvshens.com/girl/26920/",
        #  "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        name =  response.xpath('//*[@id="dmain"]/h1/text()').extract()[0]
        print(name)
        #  filename = response.url.split("/")[-2]
        #  with open(filename, 'wb') as f:
            #  f.write(response.body)
