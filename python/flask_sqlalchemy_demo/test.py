#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:
#   启动 python run.py
#   创建书籍
#   curl -X POST localhost:5000/book -H "Content-Type:application/json" -d '{"name":"wxnacy"}'
#  {
    #  "id": 94,
    #  "name": "wxnacy"
#  }
#   获取数据
#   curl localhost:5000/book/94



from flask import Flask
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wxnacy@127.0.0.1:3306/study?charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.INT, primary_key=True)
    name = db.Column(db.String, default="")

    def format(self):
        return dict(id=self.id, name=self.name)


@app.route('/book', methods=['POST'])
def create_book():
    args = request.json
    book = Book(**args)
    db.session.add(book)
    db.session.commit()
    return jsonify(book.format())

@app.route('/book/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.filter_by(id=id).first()
    return jsonify(book.format())

#  items = db.session.query(Book).order_by('id desc').all()
#  print(items)
#  for item in items:
    #  print(item)

#  items = db.session.query(Book.id, func.count(Book.id)).group_by(Book.id).all()
items = db.session.query(Book).group_by(Book.id).all()
print(items)
