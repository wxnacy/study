#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime 

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wxnacy@127.0.0.1:3306/study?charset=utf8mb4'
engine = db.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base = declarative_base()
class AlembicTest(Base):
    __tablename__ = 'alembic_test'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(132), default="s", doc="名字")
    create_ts = db.Column(db.TIMESTAMP, default='2018-01-01')
Base.metadata.create_all(engine)
Base.metadata.drop_all(engine)
