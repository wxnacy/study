#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''models'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseModel
from app.common.md import Markdown
from app.common.security import Md5
from app.config import db
from app.config import BaseConfig
from datetime import datetime
from sqlalchemy.orm import backref as b
from sqlalchemy import desc
from sqlalchemy import or_
from flask import request
import os
import re


class User(BaseModel,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.BIGINT,primary_key=True)
    name = db.Column(db.String(32),default="")
    password = db.Column(db.String(256),default="")
    ext_property = db.Column(db.JSON,default={})
    is_available = db.Column(db.INT,default=1)
    create_ts = db.Column(db.TIMESTAMP,default=datetime.now())
    update_ts = db.Column(db.TIMESTAMP,default=datetime.now())

    def is_active(self):
        return self.id != None

    def is_authenticated(self):
        return self.id != None

    def get_id(self):
        return self.id;

    def is_anonymous(self):
        return self.id == None
