#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from celery import Celery
from flask import Flask

app = Flask(__name__)

app.config.from_mapping({
    'CELERY_BROKER_URL': 'redis://localhost:6379',
    'CELERY_RESULT_BACKEND': 'redis://localhost:6379'
})

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

celery = make_celery(app)
logger = app.logger
