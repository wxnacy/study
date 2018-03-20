#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from flask import Flask
from flask import render_template
from flask import redirect
from flask_login import login_user
from models import User

from config import app
from config import login_manager

user = User(1, 'wxnacy')

@app.route('/login')
def login():
    login_user(user)
    return redirect('index')

@app.route('/index')
def index():
    return render_template('index.html')

@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return user

