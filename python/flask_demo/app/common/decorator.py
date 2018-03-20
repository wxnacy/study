#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''装饰器'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from datetime import timedelta
from flask import make_response
from flask import current_app
from flask import request
from flask import Response
from flask import g
from flask import jsonify
from functools import wraps
from functools import update_wrapper
import time

from app.common.base import BaseResponse


def jsonp(func):
    """Wraps JSONified output for JSONP requests."""

    @wraps(func)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            data = str(func(*args, **kwargs).data)
            content = str(callback) + '(' + data + ')'
            mimetype = 'application/javascript'
            return current_app.response_class(content, mimetype=mimetype)
        else:
            return func(*args, **kwargs)

    return decorated_function


def cross_domain(origin=None, methods=None, headers=None,
                 max_age=21600, attach_to_all=True,
                 automatic_options=True):
    """跨域"""
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)

    return decorator


def login_required(f):
    """如果用户没有登录，返回错误"""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return BaseResponse.return_unauthorized()
        return f(*args, **kwargs)

    return decorated_function


def args_required(*params):
    """
    检查参数
    """

    def _wrapper(func):
        @wraps(func)
        def _wrapped(*args, **kwargs):
            content_type = request.content_type
            _args = None
            if content_type == 'application/x-www-form-urlencoded':
                _args = request.form
            elif content_type == 'application/json':
                _args = request.json
            else:
                _args = request.args
            diff = list(params) - dict.fromkeys(list(_args.keys())).keys()
            if diff:
                return make_response(jsonify(
                    {
                        "message": 'args {} is necessary'.format(diff),
                        "status": 403,
                        "version": int(time.time())
                    }
                ), 403)
            return func(*args, **kwargs)

        return _wrapped

    return _wrapper


def headers_required(*params):
    """
    检查参数
    """

    def _wrapper(func):
        @wraps(func)
        def _wrapped(*args, **kwargs):
            _args = request.headers
            diff = [item[0].upper() + item[1:] for item in
                    params] - dict.fromkeys(list(_args.keys())).keys()
            if diff:
                return make_response(jsonify(
                    {
                        "message": 'header {} is necessary'.format(diff),
                        "status": 403,
                        "version": int(time.time())
                    }
                ), 403)
            return func(*args, **kwargs)

        return _wrapped

    return _wrapper


def response_xml(func):
    @wraps(func)
    def _w(*args, **kwargs):
        return Response(func(*args, **kwargs),
                        content_type='text/xml; charset=utf-8')

    return _w
