#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: reverseKGroup
@time: 2020/6/22 8:52 上午
'''
from No_24.ReverseList import Node, Linked

class ReverseKGroup:
    def __init__(self, nums:list, k:int):
        self._l = Linked(nums=nums)
        self._head = self._l.create()
        self._k = k

    def _linked_reverse(self, head:Node=None)->tuple: # O(self._k)
        # if head is None:
        #     head = self._head
        move1 = head.next #确保了move1一定不为None
        move2 = move1.next
        move3 = move1
        flag = 1
        while flag < self._k and move2 is not None:
            move1.next = move2.next
            move2.next = move3
            move3 = move2
            if move1.next is None:
                break
            move2 = move1.next
            flag += 1
        return move3, move1

    def linked_reverse_group(self, head:Node): # O(n)
        if head.next is not None:
            head_middle, head_middle2 = self._linked_reverse(head=head)
            head.next = head_middle
            self.linked_reverse_group(head=head_middle2)

    def __enter__(self):
        self.linked_reverse_group(head=self._head)
        self._l.print(head=self._head.next)
        return self._head
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':
    with ReverseKGroup(nums=[1, 2, 3, 4, 5], k=2) as r1:
        pass
    with ReverseKGroup(nums=[1, 2, 3, 4, 5], k=3) as r2:
        pass
    with ReverseKGroup(nums=[1, 2, 3, 4, 5], k=4) as r3:
        pass
    with ReverseKGroup(nums=[1, 2, 3, 4, 5], k=5) as r4:
        pass
    with ReverseKGroup(nums=[1, 2, 3, 4, 5, 6], k=4) as r5:
        pass
