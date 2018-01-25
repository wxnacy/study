#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

sched = BlockingScheduler()

#  @sched.scheduled_job('interval', id='my_job1', seconds=3,
        #  start_date='2018-01-23 09:30:00',
        #  end_date='2018-01-23 18:22:00')
@sched.scheduled_job('date', id='my_job', run_date='2018-01-23 18:25:30')
def my_job():
    print(f'{datetime.now():%H:%M:%S} Hello World ')

#  sched.add_job(my_job, 'interval', seconds=5)
#  sched.add_job(my_job, 'cron', hour=17, minute=22, second=55)
sched.start()
