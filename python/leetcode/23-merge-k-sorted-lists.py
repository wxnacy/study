#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 合并K个排序链表
# 难度 难度
'''
https://leetcode-cn.com/problems/merge-k-sorted-lists/
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''

import unittest
import utils

class ListNode(object):
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
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        l1 = ListNode(0)
        l2 = l1
        val = 0
        if not lists:
            return l1.next
        while len(lists) > 1:
            val = None
            index = -1
            for i in range(len(lists)):
                if lists[i] and val is None:
                    val = lists[i].val
                    index = i
                if lists[i] and lists[i].val < val:
                    val = lists[i].val
                    index = i
            if val is None:
                break
            l2.next = ListNode(val)
            l2 = l2.next
            if lists[index].next:
                lists[index] = lists[index].next
            else:
                lists.pop(index)
        if len(lists) == 1:
            l2.next = lists[0]
        return l1.next

    def mergeKLists1(self, lists: 'List[ListNode]') -> 'ListNode':
        def merge_two_list(l1, l2):
            l3 = ListNode(0)
            l4 = l3
            while l1 and l2:
                if l1.val > l2.val:
                    l4.next = ListNode(l2.val)
                    l4 = l4.next
                    l2 = l2.next
                elif l1.val < l2.val:
                    l4.next = ListNode(l1.val)
                    l4 = l4.next
                    l1 = l1.next
                else:
                    l4.next = ListNode(l1.val)
                    l4 = l4.next
                    l1 = l1.next
                    l4.next = ListNode(l2.val)
                    l4 = l4.next
                    l2 = l2.next
            if l1:
                l4.next = l1
            else:
                l4.next = l2
            return l3.next

        def merge(l, left, right):
            if left == right:
                return l[left]

            mid = left + ( right - left ) // 2
            l1 = merge(l, left, mid)
            l2 = merge(l, mid + 1, right)
            return merge_two_list(l1, l2)

        if not lists:
            return
        return merge(lists, 0, len(lists) - 1)


s = Solution()

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def do(self, func):
        lists = [makeListNode([1, 4, 5]), makeListNode([1, 3, 4]),
            makeListNode([2, 6])]
        self.assertEqual(
            listNodeToArray(func(lists)), [1, 1, 2, 3, 4, 4, 5, 6]
        )

        lists = [makeListNode([1, 4, 5])]
        self.assertEqual(
            listNodeToArray(func(lists)), [1, 4, 5]
        )

        lists = []
        self.assertEqual(
            listNodeToArray(func(lists)), []
        )

        lists = [[], []]
        self.assertEqual(
            listNodeToArray(func(lists)), []
        )

        lists = [makeListNode([1]), makeListNode([0])]
        self.assertEqual(
            listNodeToArray(func(lists)), [0, 1]
        )

    def test_func(self):
        self.do(s.mergeKLists)
        self.do(s.mergeKLists1)

if __name__ == "__main__":
    count = 10000
    #  utils.print_func_run_time(count, mergeTwoLists,
        #  l1 = makeListNode([2, 3, 4, 7, 8, 9]), l2 = makeListNode([4, 5]))
    #  utils.print_func_run_time(count, mergeTwoLists1,
        #  l1 = makeListNode([2, 3, 4, 7, 8, 9]), l2 = makeListNode([4, 5]))
    #  utils.print_func_run_time(count, mergeTwoLists2,
        #  l1 = makeListNode([2, 3, 4, 7, 8, 9]), l2 = makeListNode([4, 5]))
    unittest.main()



