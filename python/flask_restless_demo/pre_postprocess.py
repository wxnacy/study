#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:
# 0.17.0 版本


from flask_restless import APIManager

from models import app
from models import db
from models import Book

manager = APIManager(app, flask_sqlalchemy_db=db)

def preprocessor(**kw):
    print(kw)

def postprocessor(result, **kw):
    print('postprocessor', result, kw)
    if 'search_params' in kw:
        print('is GET_MANY')
    print(kw)

    res = dict(result)
    result['data'] = res
    result['status'] = 200
    for k, v in res.items():
        result.pop(k)

manager_params = dict(
    methods=['GET', 'POST'],
    preprocessors={
        "GET_SINGLE": [preprocessor],
        "GET_MANY": [preprocessor],
    },
    postprocessors={
        "GET_SINGLE": [postprocessor],
        "GET_MANY": [postprocessor],
        "POST": [postprocessor],
    },
    allow_functions=True
)

bp = manager.create_api(Book, **manager_params)

app.run(debug=True)
