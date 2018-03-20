#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import pymysql.cursors
from urllib.parse import urlparse

URI = 'mysql+pymysql://root:wxnacy@127.0.0.1:3306/study?charset=utf8mb4'
URL_CONFIG = urlparse(URI)
print(URL_CONFIG)

class BaseDB(object):
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
        except BaseException as e:
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
        except BaseException as e:
            app.logger.error(traceback.format_exc())
            return False
        finally:
            conn.close()

if __name__ == "__main__":
    sql = 'select * from user'
    res = BaseDB.query(sql, [])
    print(res)
