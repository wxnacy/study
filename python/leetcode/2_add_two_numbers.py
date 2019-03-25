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

class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

#  先进行算数，在解析成链表，平均 124 ms ，因为两次循环，所以偏慢
#  class Solution(object):
    #  def addTwoNumbers(self, l1, l2):
        #  """
        #  :type l1: ListNode
        #  :type l2: ListNode
        #  :rtype: ListNode
        #  """
        #  n1 = 0
        #  n2 = 0
        #  n = 0
        #  while l1 or l2:
            #  n1 += l1.val * ( 10 ** n ) if l1 else 0
            #  n2 += l2.val * ( 10 ** n ) if l2 else 0
            #  l1 = l1.next if l1 else None
            #  l2 = l2.next if l2 else None
            #  n += 1
        #  n3 = n1 + n2
        #  l3 = ListNode(0)
        #  l4 = l3
        #  while n3 >= 0:
            #  pre = n3 % 10
            #  n3 = ( n3 - pre ) // 10
            #  l4.next = ListNode(pre)
            #  l4 = l4.next
            #  if n3 == 0:
                #  n3 = -1
        #  return l3.next

# 使用一次循环，再循环的时候就计算，并输出链表，平均 80 ms
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        next_n = 0
        l3 = ListNode(0)
        temp = l3
        while l1 or l2 or next_n:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            n = n1 + n2 + next_n
            pre = n % 10
            next_n = 1 if n >= 10 else 0
            temp.next = ListNode(pre)
            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return l3.next

def makeListNode(arr: list):
    ln = ListNode(0)
    l = ln
    for i in arr:
        l.next = ListNode(i)
        l = l.next
    return ln.next

def listNodeToArray(l: ListNode):
    arr = []
    while l:
        arr.append(l.val)
        l = l.next
    return arr


if __name__ == "__main__":
    s = Solution()

    l3 = s.addTwoNumbers(makeListNode([2, 4, 3]), makeListNode([5, 6, 4]))
    print(listNodeToArray(l3) == [7, 0, 8])

    l3 = s.addTwoNumbers(makeListNode([0]), makeListNode([0]))
    print(listNodeToArray(l3) == [0])

    l3 = s.addTwoNumbers(makeListNode([1, 8]), makeListNode([0]))
    print(listNodeToArray(l3) == [1, 8])

    l3 = s.addTwoNumbers(makeListNode([5]), makeListNode([5]))
    #  print(listNodeToArray(l3))
    print(listNodeToArray(l3) == [0, 1])
