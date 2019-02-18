#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import scrapy
from first.items import GirlItem

def get_rank_urls(type='neidi'):
    res = []
    for i in range(5):
        if i == 0:
            res.append("https://m.nvshens.com/rank/")
        else:
            res.append("https://m.nvshens.com/rank/{}.html".format(i+1))
    return res

start_urls = get_rank_urls()
print(start_urls)


class RankSpider(scrapy.Spider):
    name = "rank"
    allowed_domains = ["nvshens.com"]
    start_urls = start_urls
    def parse(self, response):
        item = GirlItem()
        urls =  response.xpath('//*[@id="dlist"]/div/div/a/@href').extract()
        names = response.xpath('//*[@id="dlist"]/div/div/div/div[1]/div/span/text()').extract()
        ranks = response.xpath('//*[@id="dlist"]/div/div/div/div[5]/span/text()').extract()
        print(urls)
        print(names)
        print(ranks)

        for i in range(len(urls)):
            item['id'] = parse_id(urls[i])
            item['name'] = names[i]
            item['url'] = urls[i]
            item['poster'] = get_poster_by_id(item['id'])
            item['rank'] = ranks[i]
            yield item

def parse_id(url):
    urls = url.split("/")
    id = 0
    for i in range(len(urls)):
        if urls[i] == 'girl':
            id = urls[i+1]
    return id

def get_poster_by_id(id):
    url = 'https://img.onvshen.com:85/girl/{}/{}.jpg'.format(id, id)
    return url
