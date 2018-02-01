#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from flask import Flask
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

from datetime import datetime
from sqlalchemy.orm import backref as b

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wxnacy@127.0.0.1:3306/study?charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db=db)


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.BIGINT, primary_key=True)
    name = db.Column(db.String, default="", doc='名称')

manager.create_api(Book, allow_functions=True, methods=['GET', 'POST', 'PUT', 'DELETE'])

app.run()
