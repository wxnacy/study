#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 二叉树的最大深度 简单

'''
https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
'''

# Definition for a binary tree node.
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''

        执行用时 : 64 ms, 在Maximum Depth of Binary Tree的Python3提交中击败了90.31% 的用户
        内存消耗 : 14.4 MB, 在Maximum Depth of Binary Tree的Python3提交中击败了97.47% 的用户
        '''
        stack = []
        depth = 0
        if not root:
            return depth
        stack.append((1, root))
        while stack:
            current_depth, root = stack.pop()
            if root:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return stack

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
        self.assertEqual(1, 1)
        pass

    def test_func(self):
        self.do(s.maxDepth)

if __name__ == "__main__":
    unittest.main()
        
