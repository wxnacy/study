#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

def array2listnode(arr: list):
    '''数组转为链表'''
    ln = ListNode(0)
    l = ln
    for i in arr:
        l.next = ListNode(i)
        l = l.next
    return ln.next

def listnode2array(ln: ListNode):
    '''链表转为数组'''
    arr = []
    while ln:
        arr.append(ln.val)
        ln = ln.next
    return arr
