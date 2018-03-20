#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from flask import Flask
from flask import flash
from flask import render_template
from flask import redirect
from flask_login import LoginManager
from flask_login import login_user
from models import User

app = Flask(__name__)
app.secret_key = 'default'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.refresh_view = 'refresh_user.refresh'
login_manager.needs_refresh_message = (
            u"To protect your account, please reauthenticate to access this page."
        )
