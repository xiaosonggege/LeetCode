#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: removeNthFromEnd
@time: 2020/6/15 10:23 上午
'''
from No_24.ReverseList import Node, Linked
class RemoveNthFromEnd(Linked):
    def __init__(self, nums:list, N:int, head:Node=None):
        super().__init__(nums=nums)
        self._N = N
        self._head = self.create()

    def getnew(self): #O(n)
        move1 = self._head.next
        move2 = self._head
        flag = 0
        while flag < self._N and move1 is not None:
            move1 = move1.next
            flag += 1
        if flag == self._N:
            while move1 is not None:
                move1 = move1.next
                move2 = move2.next
            move2.next = move2.next.next

    def __enter__(self):
        self.getnew()
        self.print(head=self._head.next)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with RemoveNthFromEnd(nums=[1, 2, 3, 4, 5], N=1):
        pass
    # with RemoveNthFromEnd(nums=[1, 2, 3, 4, 5], N=2):
    #     pass
    # with RemoveNthFromEnd(nums=[1, 2, 3, 4, 5], N=3):
    #     pass
    # with RemoveNthFromEnd(nums=[1, 2, 3, 4, 5], N=4):
    #     pass
    # with RemoveNthFromEnd(nums=[1, 2, 3, 4, 5], N=5):
    #     pass
    # with RemoveNthFromEnd(nums=[1, 2, 3, 4, 5], N=6):
    #     pass