#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

class User():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'id: {id}, name: {name}'

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def get_id(self):
        return self.id;

    def is_anonymous(self):
        return False
