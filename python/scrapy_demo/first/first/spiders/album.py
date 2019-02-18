#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import scrapy
import json
from first.items import AlbumItem

surls = []
with open('girl_neidi.json') as f:
    text = f.read()
    data = json.loads(text)
    for i in data:
        surls.append("https://m.nvshens.com/girl/{}/album/".format(i['id']))

print(surls)


class AlbumSpider(scrapy.Spider):
    name = "album"
    allowed_domains = ["nvshens.com"]
    start_urls = surls

    def parse(self, response):
        name =  response.xpath('//*[@id="dmain"]/a[1]/@title').extract()[0]
        url =  response.xpath('//*[@id="dmain"]/a[1]/@href').extract()[0]
        print(url)
        urls =  response.xpath('//*[@id="dphoto"]/div/div/a/@href').extract()
        print(urls)
        names =  response.xpath('//*[@id="dphoto"]/div/div/div/div/text()').extract()
        print(names)

        for i in range(len(urls)):
            item = AlbumItem()
            item['id'] = parse_album_id(urls[i])
            item['name'] = names[i]
            item['url'] = urls[i]
            item['girl_id'] = parse_girl_id(response.url)
            item['girl_name'] = name
            item['poster'] = get_poster(item['girl_id'], item['id'])
            yield item

def parse_girl_id(url):
    us = url.split("/")
    id = 0
    for i in range(len(us)):
        if us[i] == 'girl':
            id = us[i+1]
    return id

def parse_album_id(url):
    uas = url.split("/")
    id = 0
    for i in range(len(uas)):
        if uas[i] == 'g':
            id = uas[i+1]
    return id

def get_poster(girl_id, album_id):
    url = 'https://img.onvshen.com:85/gallery/{}/{}/cover/0.jpg'.format(
            girl_id, album_id
            )
    return url

