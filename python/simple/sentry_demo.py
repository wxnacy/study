#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask import Flask
import time

sentry_sdk.init(
    dsn="https://7ad8a2c181b84f87a406a1e32363c74b@sentry.io/1800264",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)

@app.route('/debug-sentry')
def trigger_error():
    #  division_by_zero = 1 / 0
    time.tim()

@app.errorhandler(Exception)
def app_error_handler(e):
    #  logger.error(e)
    #  logger.error(traceback.format_exc())
    return 'Hello World'


app.run(debug=True)
