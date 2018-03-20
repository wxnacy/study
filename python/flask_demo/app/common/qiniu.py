#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' aliyun 的工具类'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

import oss2
import requests
from datetime import date
from datetime import datetime

access_key = '9I1VpgURzvT6t7Zb'
secret_key = 'JVXlHhYcZbFJ0cqLxJs9ySLo0IZuak'
endpoint = 'http://oss-cn-beijing.aliyuncs.com'
BUCKET_IMG = 'img-easyjava-net'


# auth = oss2.Auth(access_key, secret_key)
# service = oss2.Service(auth, endpoint)
# oss2.CaseInsensitiveDict

class OSSClient():
    def __init__(self, access_key, secret_key):
        self.auth = oss2.Auth(access_key, secret_key)

    def put_object(self, bucket_name, key, data, headers=None):
        """
        上传文本到aliyun
        :param bucket_name:
        :param key:
        :param data:
        :param content_type:
        :return:
        """
        try:
            bucket = oss2.Bucket(self.auth, endpoint, bucket_name)
            result = bucket.put_object(key, data, headers=headers)
            print(result)
            if result.status == 200:
                return 'http://%s/%s' % (bucket_name.replace('-', '.'), key)
            else:
                return None
        except BaseException as e:
            print(e)
            return None
        pass


# def put_object_from_url(bucket_name, key, url):
#     """
#     上url地址流到aliyun
#     :param bucket_name:
#     :param key:
#     :param url:
#     :return:
#     """
#     try:
#         bucket = oss2.Bucket(auth, endpoint, bucket_name)
#         input = requests.get(url)
#         result = bucket.put_object(key, input, headers={
#             'Content-Type': input.headers['Content-Type']})
#         if result.status == 200:
#             return 'http://%s/%s' % (bucket_name.replace('-', '.'), key)
#         else:
#             return None
#     except BaseException as e:
#         print(e)
#         return None
#     pass
#
#
# def put_object_from_file(bucket_name, key, file_path):
#     """
#     上传文件
#     :param bucket_name:
#     :param key:
#     :param file_path:
#     :return:
#     """
#     try:
#         bucket = oss2.Bucket(auth, endpoint, bucket_name)
#         result = bucket.put_object_from_file(key, file_path)
#         if result.status == 200:
#             return 'http://%s/%s' % (bucket_name.replace('-', '.'), key)
#         else:
#             return None
#     except IOError as e:
#         print('IOError', e)
#         return None
#     pass


if __name__ == '__main__':
    oss = OSSClient(access_key, secret_key)
    oss.put_object('file-easyjava-net',
                   'test/{}/{}.json'.format(date.today().isoformat(),
                                            datetime.utcnow().timestamp()),
                   '{"id":1}')
    pass
