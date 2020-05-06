#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: hasCycle
@time: 2020/5/5 2:30 下午
'''
from collections import namedtuple
import copy

class ListNode:
    def __init__(self, val:int=0, next=None):
        self.val = val
        self.next = next

    def _replace(self, **kwargs):
        for key, values in kwargs.items():
            self.__dict__[key] = values

class LinkedList:
    def __init__(self, head:list, pos:int):
        self._head = copy.deepcopy(head)
        self._pos = pos
        self._headNode = ListNode() #头结点

    def _create(self):
        movenode = self._headNode
        finalnext = None
        flag = 0
        for i in self._head:
            l = ListNode(val=i, next=movenode.next)
            movenode._replace(next=l)
            movenode = movenode.next
            if flag == self._pos:
                finalnext = movenode
            flag += 1
        movenode._replace(next=finalnext)

    def _hascycle(self):
        idlist = []
        node = self._headNode
        while node:
            if node in idlist:
                print('True')
                break
            else:
                idlist.append(node)
                node = node.next
                if node is None:
                    print('False')

    def __enter__(self):
        self._create()
        self._hascycle()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with LinkedList([3, 2, 0, -4], 1) as l:
        pass
    with LinkedList([1, 2], 0) as m:
        pass
    with LinkedList([1], -1) as n:
        pass