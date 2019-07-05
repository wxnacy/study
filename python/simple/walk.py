#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 实现类似 os.walk() 函数的功能

import os

def walk(path, topdown=True, followlinks=False):
    works = [path]
    while works:
        root = works[0]
        dirs = []
        files = []
        names = os.listdir(root)
        for n in names:
            p = os.path.join(root, n)
            if os.path.isdir(p):
                dirs.append(n)
            else:
                files.append(n)
        yield root, dirs, files
        works.pop(0)
        for n in dirs:
            p = os.path.join(root, n)
            if not os.path.islink(p):
                works.append(p)

def walk1(top, topdown=True, followlinks=False):
    works = [top]
    while works:
        root = works[0]
        dirs = []
        files = []
        names = os.listdir(root)
        for n in names:
            p = os.path.join(root, n)
            if os.path.isdir(p):
                dirs.append(n)
            else:
                files.append(n)
        yield root, dirs, files
        for n in dirs:
            p = os.path.join(root, n)
            if followlinks or not os.path.islink(p):
                yield from walk1(top, topdown)

#  def walk1(path, topdown=True, followlinks=False):
    #  works = [path]
    #  while works:
        #  root = works[0]
        #  dirs = []
        #  files = []
        #  names = os.listdir(root)
        #  for n in names:
            #  p = os.path.join(root, n)
            #  if os.path.isdir(p):
                #  dirs.append(n)
            #  else:
                #  files.append(n)
        #  if topdown:
            #  yield root, dirs, files
            #  works.pop(0)
            #  for n in dirs:
                #  p = os.path.join(root, n)
                #  if followlinks or not os.path.islink(p):
                    #  works.append(p)
        #  else:
            #  for w in works:
                #  yield from walk1(w, topdown, followlinks)
            #  yield root, dirs, files

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
        for path in ("/Users/wxnacy/Projects/test/walk",
            "/Users/wxnacy/Projects/test/walk/"):
            ow = os.walk(path, )
            w = func(path)
            for o in ow:
                self.assertEqual(o, next(w))

    def test_func(self):
        self.do(walk)
        self.do(walk1)

if __name__ == "__main__":
    unittest.main()

