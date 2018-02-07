#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
from graphene_sqlalchemy import SQLAlchemyObjectType
import graphene
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

class BookQuery(SQLAlchemyObjectType):
    class Meta:
        model = Book

class Query(graphene.ObjectType):
    books = graphene.List(BookQuery)

    def resolve_books(self, info):
        print(info)
        query = BookQuery.get_query(info)  # SQLAlchemy query
        return query.all()

schema = graphene.Schema(query=Query)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql',
    schema=schema, graphiql=True))

app.run(port=4901)
