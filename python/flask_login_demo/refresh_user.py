#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from flask import Flask
from flask import redirect
from models import User

from config import app
from config import login_manager
from flask_login import current_user

@app.route('/refresh')
def refresh():
    """
    https://flask-login.readthedocs.io/en/latest/#flask_login.LoginManager.needs_refresh
    """
    login_manager.needs_refresh()
    return redirect('index')


@login_manager.needs_refresh_handler
def refresh_handler():
    current_user.name = 'win'
    return redirect('index')

