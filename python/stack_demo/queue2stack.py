#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 两个队列实现一个栈

class Stack():

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, obj):
        '''
        入栈，时间复杂度 O(1)
        '''
        self.queue1.append(obj)

    def pop(self):
        '''
        出栈，时间复杂度 O(n)
        '''
        if not self.queue1:
            return None
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        self.queue1, self.queue2 = self.queue2, self.queue1
        return self.queue2.pop()

if __name__ == "__main__":
    s = Stack()
    inarr = list(range(5))
    for i in inarr:
        s.push(i)

    outarr = []
    for i in inarr:
        outarr.append(s.pop())
    print('进栈: ', inarr)
    print('出栈: ', outarr)


