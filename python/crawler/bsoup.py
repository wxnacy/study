#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import requests
from bs4 import BeautifulSoup

url = 'https://www.814aa.com/htm/downlist5/'
res = requests.get(url)

soup = BeautifulSoup(res.text)
links = soup.find_all('li')
for link in links:
    print(link)
    print(link.find('a').get('src'))
