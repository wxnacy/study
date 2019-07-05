#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 字符串压缩算法
# aabbbccccdef  =>  a2b3c4d1e1f1

def compress(s):
    if not s:
        return s
    tmp = [s[0]]
    res = ''
    for i in range(1, len(s)):
        if tmp[-1] == s[i]:
            tmp.append(s[i])
        else:
            res = f"{res}{tmp[-1]}{len(tmp)}"
            tmp = [s[i]]
    res = f"{res}{tmp[-1]}{len(tmp)}"
    return res

def decompress(s):
    if not s:
        return s
    res = []
    for i in range(0, len(s), 2):
        res.extend([s[i]] * int(s[i + 1]))
    return ''.join(res)


import unittest

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def do(self, func):
        '''todo'''
        s = "aabbbccccdef"
        res = "a2b3c4d1e1f1"
        self.assertEqual(decompress(func(s)), s)
        pass

    def test_func(self):
        self.do(compress)

if __name__ == "__main__":
    unittest.main()




