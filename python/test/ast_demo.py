#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import ast

expr = """
def add(*args):
    return args[0] + args[1]
"""

expr_ast = ast.parse(expr)
print(expr_ast)
print(ast.dump(expr_ast))
#  print(expr_ast.add(1, 2))
