#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''ElasticSearch的工具类'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.config import app
from elasticsearch.client import query_params
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from elasticsearch import RequestsHttpConnection
import time
import traceback

es = Elasticsearch(
    hosts=[{'host': app.config['ES_HOST'], 'port': app.config['ES_PORT']}],
    http_auth=app.config['ES_HTTP_AUTH'],
    use_ssl=app.config['ES_USE_SSL'],
    verify_certs=True,
    connection_class=RequestsHttpConnection
)


def create_index(index, doc_type, id, body):
    """创建索引"""
    try:
        es.create(index=index, doc_type=doc_type, id=id, body=body)
        return True
    except Exception:
        app.logger.error(traceback.format_exc())
        return False


def sync_index(index, doc_type, id, body):
    """刷新索引"""
    is_exists = exists(index, doc_type, id)
    if is_exists:
        delete_index(index, doc_type, id)

    if body:
        return create_index(index, doc_type, id, body)
    else:
        return False


def bulk_create_index(index, doc_type, bodys):
    """批量添加索引"""
    try:
        actions = make_actions(index, doc_type, 'create', bodys)
        helpers.bulk(es, actions)
        return True
    except Exception:
        app.logger.error(traceback.format_exc())
        return False


def bulk_delete_index(index, doc_type, bodys):
    """批量删除索引"""
    try:
        actions = make_actions(index, doc_type, 'delete', bodys)
        helpers.bulk(es, actions)
        return True
    except Exception:
        app.logger.error(traceback.format_exc())
        return False


@query_params('_source_include', '_source_exclude')
def get_index(index, doc_type, id, params=None):
    """通过id获取索引"""
    try:
        return es.get_source(
            index=index,
            doc_type=doc_type,
            id=id,
            params=params
        )
    except Exception:
        app.logger.error(traceback.format_exc())
        return None


def delete_index(index, doc_type, id):
    """删除索引"""
    try:
        es.delete(index=index, doc_type=doc_type, id=id)
        return True
    except Exception:
        app.logger.error(traceback.format_exc())
        return False


def delete_index_by_type(index, doc_type):
    """删除type下的所以索引"""
    try:
        res = es.delete_by_query(index=index, doc_type=doc_type, body={})
        return True
    except Exception:
        app.logger.error(traceback.format_exc())
        return False


def make_actions(index, type, action, items):
    """
    生成批量操作的集合
    :param index:
    :param type:
    :param action: 动作
    :param items: 数据集合
    :return:
    """
    actions = []
    for item in items:
        act = {
            "_index": index,
            '_op_type': action,
            "_type": type,
            "_id": item['id']
        }
        if len(item.keys()) > 1:
            act['_source'] = item

        actions.append(act)

    return actions


@query_params('_source_include', '_source_exclude', 'sort', 'page', 'size', 'q')
def search(index=None, doc_type=None, body=None, params=None):
    """
    搜索方法
    :param index: 索引
    :param doc_type:
    :param body:
    :param params: 额外参数
    :return:
    """
    # 将 page、size格式化为es参数
    size = 10
    if 'size' in params:
        size = params['size']
    if 'page' in params:
        from_ = (int(params['page']) - 1) * int(size)
        params['from_'] = from_
        del params['page']

    # *_pinyin 作为不返回参数列表默认值
    _source_exclude = ['*_pinyin']
    params['_source_exclude'] = _source_exclude

    # 当不搜索关键词时，default_operator 使用es默认值
    if 'q' in params:
        params['default_operator'] = 'AND'

    params['search_type'] = 'dfs_query_then_fetch'

    try:
        data = es.search(index=index,
                         body=body,
                         doc_type=doc_type,
                         params=params)

        results = []
        # 格式化返回数据
        if data['hits']['total'] != 0:
            res = data['hits']['hits']
            for i in res:
                results.append(i['_source'])
        total = int(data['hits']['total'])

        return results, total
    except Exception:
        app.logger.error(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        app.logger.error(traceback.format_exc())
        return [], 0


def exists(index, doc_type, id):
    '''判断索引是否存在'''
    try:
        return es.exists(index=index, doc_type=doc_type, id=id)
    except Exception:
        app.logger.error(traceback.format_exc())
        return False
