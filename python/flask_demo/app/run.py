#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''公共需要run的项目'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseResponse
from app.config import BaseConfig
from app.config import app
from app.config import db
from app import models
from app.views.html import html_bp
from app.views.api import api_bp

from flask_restless import APIManager
import traceback
import inspect
import importlib
import os

'''=================== for blueprint ============================='''
views_path = '{}/app/views/'.format(os.getcwd())
views_files = list(filter(lambda x: not x.startswith('__'),
    os.listdir(views_path)))
for path in views_files:
    module_name = 'app.views.{}'.format(path[0:-3])
    print(module_name)
    views_module = importlib.import_module(module_name)
    for name, obj in inspect.getmembers(views_module):
        if obj.__class__.__name__ == 'Blueprint':
            app.register_blueprint(obj, url_prefix = '/api')

'''=================== for restless ============================='''
manager = APIManager(app, flask_sqlalchemy_db=db)
screen_api_params = dict(
    methods=['GET'],
    results_per_page=10,
    allow_functions=True,
    url_prefix = '/restless'
)

for name, obj in inspect.getmembers(models):
    if inspect.isclass(obj) and hasattr(obj, '__tablename__'):
        manager.create_api(obj, **screen_api_params)


@app.errorhandler(Exception)
def app_error_handler(e):
    app.logger.error(traceback.format_exc())
    return BaseResponse.return_internal_server_error(str(e))
