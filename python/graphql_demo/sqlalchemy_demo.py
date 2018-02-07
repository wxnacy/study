#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wxnacy@127.0.0.1:3306/study?charset=utf8mb4'

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(132))

    def __str__(self):
        return f"Book[id:{self.id}, name:{self.name}]"


class BookQuery(SQLAlchemyObjectType):
    class Meta:
        model = Book

class Query(graphene.ObjectType):
    books = graphene.List(BookQuery)
    book = BookQuery

    def resolve_books(self, info):
        print(info)
        query = BookQuery.get_query(info)  # SQLAlchemy query
        return query.all()

    def resolve_book(self, info):
        query = BookQuery.get_query(info)  # SQLAlchemy query
        return query.filter(Book.id==2).first()

schema = graphene.Schema(query=Query)


query = '''
        query {
            books {
                name
            }
            book
        }
'''.strip()
result = schema.execute(query, context_value={'session': session})
print(result.data)
