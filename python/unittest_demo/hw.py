#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import unittest

class Test(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(11, len('Hello World'))

if __name__ == "__main__":
    unittest.main()
