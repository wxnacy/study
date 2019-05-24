#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 对称二叉树 简单

'''
https://leetcode-cn.com/problems/symmetric-tree/

给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
'''

# Definition for a binary tree node.
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    def isSymmetric1(self, root: TreeNode) -> bool:
        #递归
        def is_mirror(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return is_mirror(root1.left,root2.right) and is_mirror(root1.right,root2.left)
        return is_mirror(root,root)

    def isSymmetric(self, root: TreeNode) -> bool:
        '''
        执行用时 : 72 ms, 在Symmetric Tree的Python3提交中击败了32.98% 的用户
        内存消耗 : 12.8 MB, 在Symmetric Tree的Python3提交中击败了99.34% 的用户
        '''
        def is_mirror(left, right):
            if left and right:
                return left.val == right.val and \
                        is_mirror(left.left, right.right) and \
                        is_mirror(left.right, right.left)
            else:
                return left == right
        return is_mirror(root, root)

s = Solution()

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
        #  self.assertEqual(func())
        pass

    def test_func(self):
        self.do(s.isSymmetric)

if __name__ == "__main__":
    unittest.main()

