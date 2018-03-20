#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''for html views'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.config import app
from app.config import logger
from app.config import login_manager
from app.models import User
# for flask
from flask import Flask
from flask import Blueprint
from flask import render_template
from flask import redirect
from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user

html_bp = Blueprint('html', __name__)

# https://flask-login.readthedocs.io/en/latest/#anonymous-users
#  login_manager.anonymous_user = User

@html_bp.route('/login')
def login():
    user = User.query_by_id(1)
    login_user(user)
    return redirect('index')

@html_bp.route('/logout')
def logout():
    logout_user()
    return redirect('index')

@app.route('/refresh')
def refresh():
    """
    https://flask-login.readthedocs.io/en/latest/#flask_login.LoginManager.needs_refresh
    """
    login_manager.needs_refresh()
    return redirect('index')

@html_bp.route('/index')
def index():
    return render_template('index.html')

@login_manager.user_loader
def load_user(user_id):
    user = User.query_by_id(user_id)
    user.name = 'load_wxnacy'
    return user

@login_manager.needs_refresh_handler
def refresh_handler():
    current_user.name = 'refresh_wxnacy'
    logger.info('refresh')
    logger.info(current_user)
    logger.info(current_user.name)
    return redirect('iindex')
