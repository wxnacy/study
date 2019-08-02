#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from config import app
from config import celery
from config import logger

import tasks

@app.route('/hello/celery')
def hello_celery():
    logger.debug('hello_celery begin')
    tasks.hello_celery.delay('wxnacy')
    logger.debug('hello_celery end')
    return 'hello_celery'


if __name__ == "__main__":
    app.run()
