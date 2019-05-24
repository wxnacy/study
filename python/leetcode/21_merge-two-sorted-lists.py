#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 合并两个有序链表
# 难度 简单
'''
https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
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

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    '''只循环一次，但是因为要计算储存列表的最小值，所以性能并不好'''
    l3 = ListNode(0)
    l4 = l3
    l = []
    while l1 or l2 or l:
        n1 = l1.val if l1 else None
        n2 = l2.val if l2 else None
        if n1 or n1 == 0:
            l.append(n1)
        if n2 or n2 == 0:
            l.append(n2)
        if l:
            if len(l) == 1:
                n = l[0]
            else:
                n = min(*l)
            l4.next = ListNode(n)
            l4 = l4.next
            l.remove(n)
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return l3.next


def mergeTwoLists1(l1: ListNode, l2: ListNode) -> ListNode:
    '''使用回调来处理，时间并没有比循环单次更快，并且容易引发内存泄露，所以不推荐'''
    if not l1:
        return l2
    if not l2:
        return l1
    l3 = None
    if l1.val <= l2.val:
        l3 = ListNode(l1.val)
        l3.next = mergeTwoLists2(l1.next, l2)
    else:
        l3 = ListNode(l2.val)
        l3.next = mergeTwoLists2(l1, l2.next)
    return l3

def mergeTwoLists2(l1: ListNode, l2: ListNode) -> ListNode:
    '''只循环最短的次数，时间复杂度 O(n)'''
    l3 = ListNode(0)
    l4 = l3
    while l1 and l2:
        if l1.val < l2.val:
            l4.next = ListNode(l1.val)
            l4 = l4.next
            l1 = l1.next
        elif l1.val > l2.val:
            l4.next = ListNode(l2.val)
            l4 = l4.next
            l2 = l2.next
        else:
            l4.next = ListNode(l1.val)
            l4 = l4.next
            l4.next = ListNode(l2.val)
            l4 = l4.next
            l2 = l2.next
            l1 = l1.next
    if l1:
        l4.next = l1
    else:
        l4.next = l2
    return l3.next

def mergeTwoLists3(l1: ListNode, l2: ListNode) -> ListNode:
    '''只循环最短的次数，时间复杂度 O(n)'''
    l3 = ListNode(0)
    l4 = l3
    l = [0, 0]
    for i in range(len(l)):
        if not l1 or not l2:
            break
        if l1.val < l2.val:
            l4.next = ListNode(l1.val)
            l4 = l4.next
            l1 = l1.next
            l.append(0)
        elif l1.val > l2.val:
            l4.next = ListNode(l2.val)
            l4 = l4.next
            l2 = l2.next
            l.append(0)
        else:
            l4.next = ListNode(l1.val)
            l4 = l4.next
            l4.next = ListNode(l2.val)
            l4 = l4.next
            l2 = l2.next
            l1 = l1.next
            l.append(0)
            l.append(0)
    if l1:
        l4.next = l1
    else:
        l4.next = l2
    return l3.next

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def do(self, func):
        self.assertEqual(
            listNodeToArray(func(makeListNode([-9, 3]), makeListNode([5, 7]))),
            [-9, 3, 5, 7]
        )
        self.assertEqual(
            listNodeToArray(func(makeListNode([1, 2, 4]), makeListNode([1, 3, 4]))),
            [1, 1, 2, 3, 4, 4]
        )
        self.assertEqual(
            listNodeToArray(func(makeListNode([5, 6, 7]), makeListNode([1, 3, 4]))),
            [1, 3, 4, 5, 6, 7]
        )
        self.assertEqual(
            listNodeToArray(func(makeListNode([5, 6, 7]), makeListNode([1, 3, 8]))),
            [1, 3, 5, 6, 7, 8]
        )
        self.assertEqual(
            listNodeToArray(func(makeListNode([]), makeListNode([0]))),
            [0]
        )
        self.assertEqual(
            listNodeToArray(func(makeListNode([]), makeListNode([]))),
            []
        )
        self.assertEqual(
            listNodeToArray(func(makeListNode([2]), makeListNode([1]))),
            [1, 2]
        )

    def test_func(self):
        self.do(mergeTwoLists)
        self.do(mergeTwoLists1)
        self.do(mergeTwoLists2)
        self.do(mergeTwoLists3)

if __name__ == "__main__":
    count = 10000
    utils.print_func_run_time(count, mergeTwoLists,
        l1 = makeListNode([2, 3, 4, 7, 8, 9]), l2 = makeListNode([4, 5]))
    utils.print_func_run_time(count, mergeTwoLists1,
        l1 = makeListNode([2, 3, 4, 7, 8, 9]), l2 = makeListNode([4, 5]))
    utils.print_func_run_time(count, mergeTwoLists2,
        l1 = makeListNode([2, 3, 4, 7, 8, 9]), l2 = makeListNode([4, 5]))
    utils.print_func_run_time(count, mergeTwoLists3,
        l1 = makeListNode([2, 3, 4, 7, 8, 9]), l2 = makeListNode([4, 5]))
    unittest.main()



