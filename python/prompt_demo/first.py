#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from prompt_toolkit import prompt

if __name__ == '__main__':
    answer = prompt('Give me some input: ')
    print('You said: %s' % answer)
