#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wxnacy@127.0.0.1:3306/study?charset=utf8mb4'
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(132))

    def __str__(self):
        return f"Book[id:{self.id}, name:{self.name}]"

    @classmethod
    def salve_query_items(cls):
        items = session.query(cls).all()
        return items

#  Base.metadata.create_all(engine)

#  items = Book.query.all()
#  items = session.query(Book).all()
items = Book.salve_query_items()
print(items)

