#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 相同的树 简单

'''
https://leetcode-cn.com/problems/same-tree/
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false
'''

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:

    def isSameTree1(self, p: TreeNode, q: TreeNode) -> bool:
        '''
        执行用时 : 48 ms, 在Same Tree的Python3提交中击败了90.09% 的用户
        内存消耗 : 13.1 MB, 在Same Tree的Python3提交中击败了78.69% 的用户
        '''
        def is_same(m, n):
            if (m and not n) or (not m and n):
                return False
            if not m and not n:
                return True
            if n.val != m.val:
                return False
            return is_same(m.left, n.left) and is_same(m.right, n.right)
        return is_same(p, q)

        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        '''
        '''
        if p and q:
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        return p == q
