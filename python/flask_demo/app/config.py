#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''配置信息'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.id import Snowflake
from datetime import date
# for flask
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.contrib.fixers import ProxyFix

import os
import logging
from logging import Formatter


CONFIG_NAME_MAPPER = {
    'local': 'app.local_config.LocalConfig',
    'product': 'app.local_config.ProductionConfig',
    'dev': 'app.local_config.DevelopmentConfig',
    'test': 'app.local_config.TestingConfig'
}


class BaseConfig(object):
    DEBUG = False

    HEAD_AUTHORIZATION = 'authorization'

def create_app(flask_config_name=None):
    """
    创建配置
    :return:
    """
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    env_flask_config_name = os.getenv('FLASK_CONFIG')
    config_mapper_name = flask_config_name or env_flask_config_name or 'local'
    config_name = CONFIG_NAME_MAPPER[config_mapper_name]
    app.config.from_object(config_name)

    # 日志
    fmt = '[%(asctime)s] [%(levelname)s] %(message)s [in %(pathname)s:%(lineno)d]'
    #file_handler = logging.FileHandler('wxnacy.log')
    #file_handler.setLevel(logging.DEBUG)
    #file_handler.setFormatter(Formatter(fmt))
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(Formatter(fmt))
    #  hdlr = logging.handlers.RotatingFileHandler('wxnacy.log',
                                            #  'a', 10*1024*1024, 1)
    #  hdlr.setFormatter(Formatter(fmt))
    #  hdlr.setLevel(logging.DEBUG)
    #  app.logger.addHandler(hdlr)
    app.logger.addHandler(stream_handler)
    # app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.DEBUG)

    app.logger.debug('-------------------------init app-------------------------')
    return app


app = create_app()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "html.login"
#  login_manager.refresh_view = 'html.refresh'
login_manager.needs_refresh_message = (
    "To protect your account, please reauthenticate to access this page."
)
login_manager.needs_refresh_message_category = "info"
CORS(app)
logger = app.logger
db = SQLAlchemy(app)
snowflake = Snowflake(0)
