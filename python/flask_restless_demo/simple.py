#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from flask_restless import APIManager
from models import app
from models import db
from models import Book

manager = APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(Book, allow_functions=True, methods=['GET', 'POST', 'PUT', 'DELETE'])

app.run(debug=True)
