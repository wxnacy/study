# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    poster = scrapy.Field()
    pass

class GirlItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    name = scrapy.Field()
    poster = scrapy.Field()
    url = scrapy.Field()
    rank = scrapy.Field()
    pass

class AlbumItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    name = scrapy.Field()
    poster = scrapy.Field()
    url = scrapy.Field()
    girl_id = scrapy.Field()
    girl_name = scrapy.Field()
    pass
