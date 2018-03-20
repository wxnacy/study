#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import unittest

class Test(unittest.TestCase):

    def add(self):
        return 1 + 1

    def test_1(self):
        self.assertEqual(2, self.add())

    def test_2(self):
        self.assertEqual(2, self.add())

    def test_3(self):
        self.assertEqual(2, self.add())


if __name__ == "__main__":
    suite = unittest.TestSuite()

    tests = [Test("test_1"), Test("test_3"), Test("test_2")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
