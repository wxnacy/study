#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 两个栈实现一个队列

class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, obj):
        '''
        入队列，时间复杂度 O(1)
        '''
        self.stack1.append(obj)

    def pop(self):
        '''
        出队列，时间复杂度 O(n)
        '''
        if not self.stack1 and not self.stack2:
            return None

        if self.stack1:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()


if __name__ == "__main__":
    q = Queue()
    inarr = list(range(5))
    for i in inarr:
        q.push(i)

    outarr = []
    for i in inarr:
        outarr.append(q.pop())
    print('进队: ', inarr)
    print('出队: ', outarr)


