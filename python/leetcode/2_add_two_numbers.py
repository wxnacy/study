#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 两数相加

'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
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

def addTwoNumbers1(l1, l2):
    """
    先计算链表代表的数字，再相加，并转为链表
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    n1 = 0
    n2 = 0
    n = 0
    while l1 or l2:
        n1 += l1.val * ( 10 ** n ) if l1 else 0     # 计算链表代表的数字
        n2 += l2.val * ( 10 ** n ) if l2 else 0
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        n += 1
    n3 = n1 + n2                                    # 数字相加
    l3 = ListNode(0)
    l4 = l3
    while n3 >= 0:
        pre = n3 % 10                               # 末尾取余并构建链表
        n3 = ( n3 - pre ) // 10
        l4.next = ListNode(pre)
        l4 = l4.next
        if n3 == 0:
            n3 = -1
    return l3.next

def addTwoNumbers2(l1, l2):
    """
    再看下题目，发现结果链表的每位，都是传参的两个链表的每位相加得到的
    由此可以使用一次循环，直接计算每位数字并输出到链表
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    next_n = 0
    l3 = ListNode(0)
    temp = l3
    while l1 or l2 or next_n:           # l1、l2 循环后，如果有进位，在执行一次
        n1 = l1.val if l1 else 0
        n2 = l2.val if l2 else 0
        n = n1 + n2 + next_n            # 链表数字相加，并加上一个链表的进位
        pre = n % 10                    # 取余数，并构建该层链表
        next_n = 1 if n >= 10 else 0    # 判断是否有进位
        temp.next = ListNode(pre)
        temp = temp.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return l3.next


class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def test_addTwoNumbers1(self):
        l3 = addTwoNumbers1(makeListNode([2, 4, 3]), makeListNode([5, 6, 4]))
        self.assertEqual(listNodeToArray(l3), [7, 0, 8])

        l3 = addTwoNumbers1(makeListNode([0]), makeListNode([0]))
        self.assertEqual(listNodeToArray(l3), [0])

        l3 = addTwoNumbers1(makeListNode([1, 8]), makeListNode([0]))
        self.assertEqual(listNodeToArray(l3), [1, 8])

        l3 = addTwoNumbers1(makeListNode([5]), makeListNode([5]))
        self.assertEqual(listNodeToArray(l3), [0, 1])

    def test_addTwoNumbers2(self):
        l3 = addTwoNumbers2(makeListNode([2, 4, 3]), makeListNode([5, 6, 4]))
        self.assertEqual(listNodeToArray(l3), [7, 0, 8])

        l3 = addTwoNumbers2(makeListNode([0]), makeListNode([0]))
        self.assertEqual(listNodeToArray(l3), [0])

        l3 = addTwoNumbers2(makeListNode([1, 8]), makeListNode([0]))
        self.assertEqual(listNodeToArray(l3), [1, 8])

        l3 = addTwoNumbers2(makeListNode([5]), makeListNode([5]))
        self.assertEqual(listNodeToArray(l3), [0, 1])

if __name__ == "__main__":
    count = 10000
    utils.print_func_run_time(count, addTwoNumbers1,
        l1 = makeListNode([2, 4, 3]), l2 = makeListNode([5, 6, 4]))
    utils.print_func_run_time(count, addTwoNumbers2,
        l1 = makeListNode([2, 4, 3]), l2 = makeListNode([5, 6, 4]))
    unittest.main()

