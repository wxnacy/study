#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

 
from colify.colify import Colify

countries = {}
countries['spain'] = ["madrid", "barcelona", "bilbao", "Malaga"]
countries['italy'] = ["rome", "florence", "milan", "venice", "palermo", "padua"]
countries['france'] = ["paris", "lyon", "toulouse", "nantes"]

c = Colify(countries)
c.colify()
