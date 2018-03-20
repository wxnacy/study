#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from flask import Flask
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
from sqlalchemy.orm import backref as b

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wxnacy@127.0.0.1:3306/study?charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.BIGINT, primary_key=True)
    name = db.Column(db.String, default="", doc='名称')


