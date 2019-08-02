#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import time

from config import celery
from config import logger

@celery.task
def hello_celery(name):
    time.sleep(2)
    logger.debug(f'my name is {name}')
    return f'my name is {name}'

