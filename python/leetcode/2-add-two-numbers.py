#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 两数相加

'''
难度：中等

知识点：链表、数学

地址： [https://leetcode-cn.com/problems/add-two-numbers/](https://leetcode-cn.com/problems/add-two-numbers/)

```
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例:

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

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        两遍循环
        执行用时 : 108 ms, 在Add Two Numbers的Python3提交中击败了80.06% 的用户
        内存消耗 : 13.2 MB, 在Add Two Numbers的Python3提交中击败了76.78% 的用户
        '''
        n1, n2 = 0, 0
        n = 0
        while l1 or l2:
            if l1:
                n1 += l1.val * (10 ** n)
                l1 = l1.next
            if l2:
                n2 += l2.val * (10 ** n)
                l2 = l2.next
            n += 1

        n3 = n1 + n2
        if n3 == 0:
            return ListNode(0)

        l3 = ListNode(0)
        l4 = l3
        while n3 > 0:
            rmd = n3 % 10
            l4.next = ListNode(rmd)
            l4 = l4.next
            n3 = (n3 - rmd) // 10

        return l3.next

    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        一遍循环
        执行用时 : 88 ms, 在Add Two Numbers的Python3提交中击败了99.56% 的用户
        内存消耗 : 13.1 MB, 在Add Two Numbers的Python3提交中击败了90.86% 的用户
        '''
        carry = 0
        l3 = ListNode(0)
        l4 = l3
        while l1 or l2 or carry:
            n3 = carry
            if l1:
                n3 += l1.val
                l1 = l1.next
            if l2:
                n3 += l2.val
                l2 = l2.next
            carry = n3 //  10
            l4.next = ListNode(n3 % 10)
            l4 = l4.next
        return l3.next

s = Solution()

import unittest
import utils

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def do(self, func):
        '''todo'''
        lns = (
            ( [2, 4, 3], [5, 6, 4], [7, 0, 8]),
            ( [0], [0], [0]),
            ( [1, 8], [0], [1, 8]),
            ( [5], [5], [0, 1]),
        )
        for l1, l2, l3 in lns:
            l = func(utils.array2listnode(l1), utils.array2listnode(l2))
            self.assertEqual(utils.listnode2array(l), l3)

    def test_func(self):
        self.do(s.addTwoNumbers)
        self.do(s.addTwoNumbers1)

if __name__ == "__main__":
    count = 1000
    tm = TestMain()
    utils.print_unittest_do_run_time(count, tm.do, s.addTwoNumbers)
    utils.print_unittest_do_run_time(count, tm.do, s.addTwoNumbers1)
    unittest.main()

#  || .
#  || ----------------------------------------------------------------------
#  || Ran 1 test in 0.000s
#  ||
#  || OK
#  || addTwoNumbers        run 1000 times used 0.03676531100063585s
#  || addTwoNumbers1       run 1000 times used 0.033320688002277166s
