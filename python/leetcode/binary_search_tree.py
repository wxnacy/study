#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 判断二叉搜索树
'''
思路：
1、先将根节点的值跟一个最大值和最小值作比较
2、然后将根节点的值，作为左子节点的最大值和右子节点的最小值递归比较下去，直到完成。
'''

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_bst(node):
    '''判断是否为二叉搜索树'''

    def _is_bst(node, min_val, max_val):
        '''判断单个节点'''
        if node == None:
            return True

        if min_val >= node.val or node.val >= max_val:
            return False

        return _is_bst(node.left, min_val, node.val) and _is_bst(node.right, node.val, max_val)

    return _is_bst(node, -2**32, 2**32-1)

import unittest

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def test_func(self):
        n1 = Node(6)
        n1.left = Node(3)
        n1.right = Node(9)
        n1.left.left = Node(1)
        n1.left.right = Node(5)
        n1.right.left = Node(7)
        n1.right.right = Node(10)
        self.assertTrue(is_bst(n1))

        n2 = Node(5)
        n2.left = Node(1)
        n2.right = Node(6)
        n2.right.left = Node(3)
        n2.right.right = Node(7)
        self.assertFalse(is_bst(n2))

if __name__ == "__main__":
    unittest.main()


