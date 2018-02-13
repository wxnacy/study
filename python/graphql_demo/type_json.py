#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import graphene
from graphql.language.ast import BooleanValue, StringValue, IntValue, ListValue, ObjectValue, FloatValue

class JSON(graphene.Scalar):
    """
    The `JSON` scalar type represents JSON values as specified by
    [ECMA-404](http://www.ecma-international.org/
    publications/files/ECMA-ST/ECMA-404.pdf).
    """

    @staticmethod
    def identity(value):
        if isinstance(value, (str, bool, int, float)):
            return value.__class__(value)
        elif isinstance(value, (list, dict)):
            return value
        else:
            return None

    serialize = identity
    parse_value = identity

    @staticmethod
    def parse_literal(ast):
        if isinstance(ast, (StringValue, BooleanValue)):
            return ast.value
        elif isinstance(ast, IntValue):
            num = int(ast.value)
            return num
        elif isinstance(ast, FloatValue):
            return float(ast.value)
        elif isinstance(ast, ListValue):
            return [JSON.parse_literal(value) for value in ast.values]
        elif isinstance(ast, ObjectValue):
            return {field.name.value: JSON.parse_literal(field.value) for field in ast.fields}
        else:
            return None

class Query(graphene.ObjectType):
    test = graphene.Field(JSON)

    def resolve_test(self, info):
        return dict(name="wxnacy", age=12, types = ['shuaiqi', 'youcai'],
            book=dict(name='wohenshuai'))

schema = graphene.Schema(query=Query)

result = schema.execute('{ test  }')
print(result.data['test'])
