#!/usr/bin/env python
# ! -*- coding:utf-8 -*-
"""base信息"""

__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.config import app
from app.config import db
from app.config import snowflake
from app.common.security import AESecurity
from datetime import datetime, date
from flask import make_response
from flask import jsonify
from flask import request
from uuid import UUID
from sqlalchemy import desc
from sqlalchemy.ext.declarative import DeclarativeMeta
from urllib.parse import urlparse
import traceback
import json
import pymysql.cursors
import time

URL_CONFIG = urlparse(app.config['SQLALCHEMY_DATABASE_URI'])


class BaseObject(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return eval(self.to_json())

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

    def format(self):
        return self.to_dict()

    def __str__(self):
        return self.to_json()


class BaseModel(BaseObject):
    """
    SQLAlchemy JSON serialization
    """
    RELATIONSHIPS_TO_DICT = False
    __tablename__ = None

    def __iter__(self):
        return self.to_dict().iteritems()

    def extended_encoder(self, x):
        if isinstance(x, datetime):
            return int(x.timestamp())
        if isinstance(x, UUID):
            return str(x)
        if isinstance(x, date):
            return x.isoformat()
        return x

    def to_dict(self, rel=None, backref=None, **kwargs):
        if rel is None:
            rel = self.RELATIONSHIPS_TO_DICT
        res = {column.key: self.extended_encoder(getattr(self, attr))
               for attr, column in self.__mapper__.c.items()}
        if rel:
            for attr, relation in self.__mapper__.relationships.items():
                # Avoid recursive loop between to tables.
                if backref == relation.table:
                    continue
                value = getattr(self, attr)
                if value is None:
                    res[relation.key] = None
                elif isinstance(value.__class__, DeclarativeMeta):
                    res[relation.key] = value.to_dict(backref=self.__table__)
                else:
                    res[relation.key] = [i.to_dict(backref=self.__table__)
                                         for i in value]
        return BaseDict(res)

    def to_json_str(self, rel=None):
        if rel is None:
            rel = self.RELATIONSHIPS_TO_DICT
        return json.dumps(self.to_dict(rel), default=self.extended_encoder)

    def __str__(self):
        return self.to_json_str()

    @classmethod
    def generate_id(cls):
        """生成id"""
        table_name = cls.__tablename__
        return 'A{}'.format(snowflake.generate())

    @classmethod
    def create(cls, **params):
        item = cls(**params)
        db.session.add(item)
        db.session.commit()
        return item

    @classmethod
    def create_if_not_exist(cls, **params):
        item = cls.query_item(**params)
        if not item:
            item = cls.create(**params)
        return item

    def create_self(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def query_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def query_item(cls, **params):
        if not params:
            params = {}
        params['is_available'] = 1
        return cls.query.filter_by(**params).first()

    @classmethod
    def query_paginate(cls, page, per_page, **params):
        if not params:
            params = {}
        params['is_available'] = 1
        return cls.query.filter_by(**params).order_by(
            desc(cls.create_ts)).paginate(page, per_page, False)

    @classmethod
    def query_items(cls, **params):
        if not params:
            params = {}
        params['is_available'] = 1
        return cls.query.filter_by(**params).all()

    @classmethod
    def query_count(cls, **params):
        if not params:
            params = {}
        params['is_available'] = 1
        return cls.query.filter_by(**params).count()

    @classmethod
    def delete(cls, **params):
        item = cls.query.filter_by(**params).update(dict(is_available=0))
        db.session.commit()
        return item

    def delete_self(self):
        self.is_available = 0
        db.session.commit()
        return self

    @classmethod
    def update_by_id(cls, id, **params):
        item = cls.query.filter_by(id=id, is_available=1).update(params)
        db.session.commit()
        return item

    def update_self(self):
        db.session.commit()
        return self


class BaseDB():
    @classmethod
    def create_conn(cls):
        '''创建mysql链接'''
        return pymysql.connect(
            host=URL_CONFIG.hostname,
            port=URL_CONFIG.port,
            user=URL_CONFIG.username,
            password=URL_CONFIG.password,
            db=URL_CONFIG.path[1:],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    @classmethod
    def query(cls, sql, params):
        """
        查询操作
        :param sql:
        :param params:
        :return:
        """
        conn = cls.create_conn()
        try:
            cursor = conn.cursor()

            cursor.execute(sql, params)
            conn.commit()
            result = cursor.fetchall()
            cursor.close()
            return result
        except:
            app.logger.error(traceback.format_exc())
            return []
        finally:
            conn.close()

    @classmethod
    def execute(cls, sql, params):
        """
        更新操作
        :param sql:
        :param params:
        :return:
        """
        conn = cls.create_conn()
        try:
            cursor = conn.cursor()

            result = cursor.execute(sql, params)
            conn.commit()
            cursor.close()
            return result
        except:
            app.logger.error(traceback.format_exc())
            return False
        finally:
            conn.close()


class BaseResponse(BaseObject):
    data = {}
    status = 200
    message = None
    version = 0

    def __init__(self, data={}, status=200, message=""):
        self.data = data
        self.status = status
        self.message = message
        self.version = int(time.time())

    @classmethod
    def return_response(cls, data={}, status=200, message="", headers={}):
        res = cls(
            data=data,
            status=status,
            message=message
        ).to_dict()
        return make_response(jsonify(res), status, headers)

    @classmethod
    def return_success(cls, data={}):
        return cls.return_response(data)

    @classmethod
    def return_error(cls, status, message):
        return cls.return_response(status=status, message=message)

    @classmethod
    def return_internal_server_error(cls, message='Internal Server Error'):
        return cls.return_response(status=500, message=message)

    @classmethod
    def return_unauthorized(cls, message='Unauthorized'):
        return cls.return_response(status=401, message=message)

    @classmethod
    def return_not_found(cls, message='Not Found'):
        return cls.return_response(status=404, message=message)

    @classmethod
    def return_forbidden(cls, message='Forbidden'):
        return cls.return_response(status=403, message=message)

    @classmethod
    def make_paginate(cls, data, total, page, per_page):
        """
        生成返回数据
        :param list:
        :param total_size:
        :param page:
        :param size:
        :return:
        """
        total_page = total // per_page
        yu = total % per_page
        if yu > 0:
            total_page += 1

        res = {
            "items": data,
            "page": int(page),
            "total": total,
            "total_pages": total_page,
            "per_page": per_page
        }
        return res


class BaseRequest():
    @classmethod
    def get_arg_int(cls, params, key, default=0):
        res = params.get(key, default)
        if not res:
            return default
        return int(res)

    @classmethod
    def get_args(cls):
        content_type = request.content_type
        if content_type == 'application/x-www-form-urlencoded':
            _args = request.form
        elif content_type == 'application/json':
            _args = request.json
        else:
            _args = request.args
        return _args


class BaseDict(dict):
    def filter(self, *args, **kwargs):
        """
        过滤dict
        :param args: 默认 source_include
        :param kwargs:
            source_include：想要留下的keys
                eq:[attr,attr1]
                子元素可以使用 ["obj.attr"] 和 ["obj[attr1,attr2]"] 两种方式
                速度上推荐使用 ["obj[attr1,attr2]"]
            source_exclude：想要去掉的keys
        :return:
        """
        source_include = args if args else kwargs.get('source_include')
        source_exclude = kwargs.get('source_exclude')

        def _filter(t, o, k):
            """
            过滤key
            :param t: 过滤结果
            :param o: 目标对象
            :param k: 需要过滤的key
            :return:
            """
            if k in o:
                t[k] = o[k]
            return t

        def _check_key(t, o, k):
            """
            判断key需要何种过滤
            :param t: 过滤结果
            :param o: 目标对象
            :param k: 需要过滤的key
            :return:
            """
            if '.' in k:
                key = k.split('.', 1)[0]
                sub_key = k.split('.', 1)[1]
                if o.get(key) and isinstance(o.get(key), dict):
                    if key not in t:
                        t[key] = {}
                    t[key] = _check_key(t[key], o[key], sub_key)
            elif '[' in k and ']' in k:
                key = k.split('[')[0]
                v = o.get(key)
                sub_keys = k.split('[')[1].rstrip(']').split(',')
                if isinstance(v, dict):
                    t[key] = BaseDict(v).filter(*sub_keys)
                elif isinstance(v, list):
                    t[key] = [BaseDict(sv).filter(*sub_keys) for sv in v]
            else:
                t = _filter(t, o, k)

            return t

        temp = {}
        if source_include:
            for item in source_include:
                temp = _check_key(temp, self, item)
            return temp
        elif source_exclude:
            for item in source_exclude:
                self.pop(item)
            return self
        return self


class UserSecurity():
    KEY = 'b8d4471654c7330c'
    aes = AESecurity(KEY)

    @classmethod
    def generate_authorization(cls, user_id, **params):
        '''用户id加密'''
        data = '{};{}'.format(user_id, int(time.time()))
        return cls.aes.encrypt(data)

    @classmethod
    def get_user_id(cls, authorization):
        '''从加密信息中过去用户'''
        try:
            if not authorization or authorization == 'null':
                return None
            data = cls.aes.decrypt(authorization)
            return data.split(';')[0]
        except:
            app.logger.error(traceback.format_exc())
            return None


if __name__ == '__main__':
    id = BaseModel.generate_id()
    token = UserSecurity.generate_authorization(id)
    print(token)
    print(UserSecurity.get_user_id(token))
