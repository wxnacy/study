#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import records

db = records.Database('mysql+pymysql://root:wxnacy@127.0.0.1:3306/study?charset=utf8mb4')

rows = db.query('select * from user')
print(rows.dataset)
print(rows.first())

#  with open('/tmp/report.xls', 'wb') as f:
    #  f.write(rows.export('xls'))
