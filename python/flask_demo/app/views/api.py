#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''views'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseResponse
from app.common.decorator import args_required
from flask import Blueprint

api_bp = Blueprint('api', __name__)


@api_bp.route('/test', methods=['GET', 'POST'])
@args_required('name')
def test():
    ''''''
    return BaseResponse.return_success()
