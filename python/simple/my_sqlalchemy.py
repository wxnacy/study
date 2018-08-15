#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from sqlalchemy import or_
from sqlalchemy import text
from collections import namedtuple

Base = declarative_base()

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wxnacy@127.0.0.1:3306/study?charset=utf8mb4'
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(132))
    
    def __str__(self):
        return f"Book[id:{self.id}, name:{self.name}]"

# 创建表
#  Base.metadata.create_all(engine)

# 添加数据
#  book = Book(name="new book")
#  session.add(book)
#  session.commit()

# insert into book (name) values ('wxnacy');
# insert into book (name) values ('wxnacy');
#  session.add(Book(name="wxnacy"))
#  session.add(Book(name="wxnacy"))
#  session.commit()

#  session.add_all([Book(name="wxnacy"), Book(name="wxnacy")])
#  session.commit()

# insert into book (name) values ('wxnacy'), ('wxnacy');
items = [dict(name="wxnacy"), dict(name="wxnacy")]
session.execute(Book.__table__.insert(), items)
session.commit()

#  books = session.query(Book).filter(and_(Book.id==2, Book.name=="new book")).all()
#  books = session.query(Book).filter(~Book.id.in_([2])).all()
#  books = session.query(Book).filter().limit(1).all()
#  for b in books:
    #  print(b)
#  print(books)

#  book = session.query(Book).filter_by(id=1).first()
#  book = session.query(Book).filter(Book.id==1).first()
#  print(book)
#  session.delete(book)
#  session.commit()


#  res = session.execute(text("select * from book where id = :id"), **dict(id=2)).fetchall()
res = engine.execute(text("insert into book (name) values (:name)"),
        **dict(name='text'))
#  print(res)
#  book = session.query(Book).filter(text("id = :id and name = :name")).params(id=2, name="new book").first()
#  print(book)
#  res = session.execute(text("select * from book where id = 2")).fetchall()
#  res = session.execute(text("select * from book where id = 2"))

#  Record = namedtuple('Record', res.keys())
#  records = {Record(*r) for r in res.fetchall()}
#  res = [r for r in records]
#  print(res)  # > [Record(id=2, name='new book')]

#  def _fmt_i(k, v):
    #  return k ,v

#  def _fmt(o):
    #  r = list(map(_fmt_i, res.keys(), o))
    #  return {k: v for k, v in r}
#  res = [_fmt(o) for o in res.fetchall()]
#  print(res)  # > [{'id': 2, 'name': 'new book'}]

#  books = session.query(Book).filter(text("id in :ids")).params(ids=[2, 3, 4, 5]).all()
#  for b in books:
    #  b.name = f'{b.id}-book'
    #  session.add(b)
#  session.commit()

res = engine.execute(text("select sum(id) from book")).fetchall()
print(res)

#  res = session.query().filter(text("id < 30")).paginate(1, 2, False)
#  res = session.query.filter(text("id < 30")).all()

res = session.query(Book).filter_by().paginate(1, 2, False)
print(res)
