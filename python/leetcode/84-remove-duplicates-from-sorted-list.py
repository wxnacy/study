#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 删除排序链表中的重复元素 简单

'''
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3
'''
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

def makeListNode(arr: list):
    '''使用数组生成链表'''
    ln = ListNode(0)
    l = ln
    for i in arr:
        l.next = ListNode(i)
        l = l.next
    return ln.next

def listNodeToArray(l: ListNode):
    '''链表转为数组'''
    arr = []
    while l:
        arr.append(l.val)
        l = l.next
    return arr

class Solution:
    def deleteDuplicates1(self, head: 'ListNode') -> 'ListNode':
        '''
        执行用时 : 80 ms, 在Remove Duplicates from Sorted List的Python3提交中击败了33.80% 的用户
        内存消耗 : 12.9 MB, 在Remove Duplicates from Sorted List的Python3提交中击败了97.66% 的用户
        '''
        nums = set()
        l = ListNode(0)
        l2 = l
        while head:
            if head.val not in nums:
                nums.add(head.val)
                l2.next = ListNode(head.val)
                l2 = l2.next
            head = head.next
        return l.next

    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        '''
        执行用时 : 60 ms, 在Remove Duplicates from Sorted List的Python3提交中击败了95.04% 的用户
        内存消耗 : 13 MB, 在Remove Duplicates from Sorted List的Python3提交中击败了95.33% 的用户
        '''
        if not head:
            return head
        l = head
        n = head.next
        while n:
            if l.val == n.val:
                l.next = n.next
            else:
                l = n
            n = n.next
        return head

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
        head = makeListNode([1, 1, 2])
        res = [1, 2]
        self.assertEqual(listNodeToArray(func(head)), res)
        head = makeListNode([1, 1, 2, 3, 3])
        res = [1, 2, 3]
        self.assertEqual(listNodeToArray(func(head)), res)
        pass

    def test_func(self):
        self.do(s.deleteDuplicates)

if __name__ == "__main__":
    unittest.main()
