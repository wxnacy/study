#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import argparse
parser = argparse.ArgumentParser(description='This is a argparse demo')
#  parser.add_argument('file', help='List file or dir')
#  parser.add_argument('-u', '--user', help='Config user name')
parser.add_argument('-H', '--headers', action='append')
args = parser.parse_args()
#  print(args.file)
#  print(args.user)
print(args.headers)
