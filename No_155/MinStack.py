#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: MinStack
@time: 2020/5/6 11:21 上午
'''
from No_141.hasCycle import ListNode

class MinStack:
    def __init__(self):
        self._head = ListNode()
        self._top = self._head
        self._min = 100

    def push(self, x:int)->None:
        l = ListNode(val=x, next=self._top.next)
        self._top._replace(next=l)
        if self._min > x:
            self._min = x

    def pop(self)->None:
        if self._top.next is None:
            print('空栈')
            return
        self._top._replace(next=self._top.next.next)

    def top(self)->int:
        if self._top.next is None:
            print('空栈')
            self._min = 0
            return
        else:
            return self._top.next.val

    def getmin(self)->int:
        return self._min

if __name__ == '__main__':
    s = MinStack()
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    print('栈顶元素:{0}, 最小元素:{1}'.format(s.top(), s.getmin()))

