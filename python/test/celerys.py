#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 

import time

from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def send_email(email):
    print('send email to', email)
    time.sleep(3)
    return 'success'

def register():
    print('begin register')
    send_email.delay('wxnacy@gmail.com')
    print('end')

if __name__ == "__main__":
    register()

