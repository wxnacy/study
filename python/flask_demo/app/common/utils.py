#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''工具类'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

import re
import random
import time
import os
import json
from math import radians, cos, sin, asin, sqrt

RE_CHINESE = re.compile(u"[\u4e00-\u9fa5]+")  # 正则查找中文
RE_ENGLISH = re.compile(u"[A-Za-z]+")  # 正则查找英文

STR = [
    '0', '1', '2', '3', '4', '5',
    '6', '7', '8', '9', 'a', 'b',
    'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]


def find_chinese(str):
    """
    查找字符串中中文集合
    :param str:
    :return:
    """
    return re.findall(RE_CHINESE, str)


def find_english(str):
    """
    查找字符串中的英文
    :param str:
    :return:
    """
    return re.findall(RE_ENGLISH, str)


def reduplicate(list):
    """
    去掉list中的重复值
    :param list:
    :return:
    """
    temp = []
    for item in list:
        if item not in temp:
            temp.append(item)
    return temp


def get_random_str(str_len):
    """
    获取随机字符串
    :param str_len: 需要获取的长度
    :return:
    """
    def _create():
        return str(STR[int(random.uniform(0, len(STR)))])
    res = [_create() for x in range(0, str_len)]
    return ''.join(res)


def generate_body_sort_script(sort='desc', **params):
    """生成es权重排序的body数据"""
    inline = []
    for key in params:
        inline.append("doc['{}'].value * params.{}".format(key, key))

    inline = "+".join(inline)

    body = {
        "sort": {
            "_script": {
                "type": "number",
                "script": {
                    "lang": "painless",
                    "inline": inline,
                    "params": params
                },
                "order": sort
            }
        }
    }
    return body


def generate_body(sort='desc', _script=None, match=None, term=None,
                  _range=None):
    '''构造esbody'''
    body = {}
    if _script:
        body = generate_body_sort_script(sort=sort, **_script)

    body['query'] = {
        "bool": {
            "must": [],
            "filter": []
        }
    }
    if match:
        for key, value in match.iteritems():
            body['query']['bool']['must'].append(
                {"match":
                    {
                        key: {
                            "query": value,
                            "operator": "and"
                        }
                    }
                }
            )

    if term:
        for key, value in term.iteritems():
            body['query']['bool']['filter'].append({"term": {key: value}})

    if _range:
        for key, value in _range.iteritems():
            body['query']['bool']['filter'].append({"range": {key: value}})

    return body


def filter_dict(json, *args, **kwargs):
    '''
    过滤json数据
    :param json:
    :param params:
    :param source_include:
    :return:
    '''

    source_include = kwargs.get('source_include')
    if args:
        source_include = list(args)
    source_exclude = kwargs.get('source_exclude')

    temp = {}
    if source_include:
        for item in source_include:
            temp[item] = json[item]
        return temp
    elif source_exclude:
        for item in source_exclude:
            del json[item]
        return json


def check_back_card(card_num):
    """检查银行卡的合法性"""
    total = 0
    even = True

    if isinstance(card_num, int):
        card_num = str(card_num)

    check_num = card_num[-1]
    for item in card_num[-2::-1]:
        item = int(item)
        if even:
            item <<= 1

        if item > 9:
            item -= 9

        total += item
        even = not even

    return int(check_num) is (10 - (total % 10)) % 10


def check_identity_card(card):
    wi = ["7", "9", "10", "5", "8", "4", "2", "1", "6", "3", "7", "9", "10",
          "5", "8", "4", "2"]
    total = 0
    card = list(card)
    index = 0
    for item in card:
        total += ord(item) * int(wi[index])
        index += 1

    t = total % 11
    r = (12 - t) % 11
    if r == 10:
        return "X"
    else:
        return r


def timer(func, *args, reps=1000, **kwargs):
    """计算方法耗时"""
    start = time.time()
    reps_list = range(reps)
    for i in reps_list:
        func(*args, **kwargs)

    elapsed = time.time() - start
    return elapsed


def test():
    print(os.getcwd())
    root_dir = os.getcwd()
    file_path = '{}/app/static/file/ss/{}.json'.format(root_dir,
                                                       get_random_str(5))
    print(file_path)
    file = open(file_path, 'w')
    data = dict(id=1, name='win')
    file.write(json.dumps(data))
    file.flush()
    file.close()


def distance_between_points(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(
        radians, [float(lon1), float(lat1), float(lon2), float(lat2)])
    # haversine 公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000     # 结果单位米



if __name__ == '__main__':
    # print(check_back_card('6225768741961625'))
    # print(check_identity_card('132201199108297010'))
    # print(check_identity_card('6225768741961625'))
    # print(vars())
    # print(vars().get('get_random_str'))
    # print(vars().get('get_random_
    location = (39.7836455948, 116.5627747582, 39.7833570280, 116.5636974381)
    print(distance_between_points(*location))   # ==> 85.12205329599756
    pass
