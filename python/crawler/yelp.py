#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 见 __main__ 方法

from requests_html import HTMLSession
import json
import sys

session = HTMLSession()

URL = 'https://www.yelp.com'

def item(url):
    '''获取单个店铺信息'''
    r = session.get(url)
    if r.status_code != 200:
        return
    html = r.html
    res = {}

    scrs = html.find('script[type="application/ld+json"]')
    json_text = scrs[1].text
    json_data = json.loads(json_text)

    mores = html.find('ul.ylist > li > div > dl')
    more = {}
    for m in mores:
        k = m.find('dt', first=True).text
        v = m.find('dd', first=True).text

        more[k] = v
    res['more'] = more

    if 'review' in json_data:
        json_data.pop('review')
    res.update(json_data)
    res['url'] = url
    priceSelector = '#wrap > div.biz-country-jp > div > div.top-shelf > div > div.biz-page-header.clearfix > div.biz-page-header-left.claim-status > div.biz-main-info.embossed-text-white > div.price-category > span.bullet-after > span'
    price = html.find(priceSelector, first = True)
    res['priceLevel'] = price.text
    return res

def search(url):
    '''抓取列表数据'''
    r = session.get(url)
    if r.status_code != 200:
        return

    html = r.html

    res = []

    # 图片
    image_selecter = 'div.lemon--div__373c0__1mboc.child__373c0__35DrB.border-color--default__373c0__2oFDT > div > a > img'
    images = html.find(image_selecter)

    # 标题
    a_selecter = 'div.lemon--div__373c0__1mboc.businessName__373c0__1fTgn.border-color--default__373c0__2oFDT > h3 > a'
    texts = html.find(a_selecter)
    for i in range(len(texts)):
        t = texts[i]
        href = t.attrs['href']
        item = dict(name = t.text, url = f'{URL}{href}')
        image = images[i]
        item['image'] = image.attrs['src']
        imageset = image.attrs['srcset']
        sets = imageset.split(',')
        item['images'] = {}
        for s in sets:
            si = s.split(" ")
            item['images'].update({si[1]: si[0]})
        res.append(item)

    return res

if __name__ == "__main__":
    '''
    抓取 yelp 数据
    Usage: python yelp.py <url>
    Eg   : python yelp.py https://www.yelp.com/search?find_desc=&find_loc=Taipei%2C+Taiwan&ns=1
            return see : https://raw.githubusercontent.com/wxnacy/image/master/common/yelp_search.png
           python yelp.py https://www.yelp.com/biz/%E6%B2%BB%E9%83%8E%E4%B8%B8-%E6%96%B0%E5%AE%BF%E6%9C%AC%E5%BA%97-%E6%96%B0%E5%AE%BF%E5%8C%BA?osq=Restaurants
            return see : https://raw.githubusercontent.com/wxnacy/image/master/common/yelp_item.png
    '''
    args = sys.argv
    if len(args) < 2:
        print('Usage: python yelp <url>')
        sys.exit(0)

    url = args[1]
    if '/search' in url:
        res = search(url)
    else:
        res = item(url)
    print(json.dumps(res))


