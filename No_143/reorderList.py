#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: reorderList
@time: 2020/6/14 10:15 上午
'''
from No_24.ReverseList import Node, Linked, Reverselist
class ReorderList(Linked):
    def __init__(self, nums:list):
        super().__init__(nums=nums)
        self._head = self.create()

    def process(self)->None: # O(n) + O(n//2) + O(n // 2) = O(n)
        # 快慢指针找到后半段链表的表头和尾
        move1 = move2 = self._head
        flag = 0
        while move2.next is not None: #O(n)
            move2 = move2.next
            flag = 1 - flag
            if flag == 0:
                move1 = move1.next
        move1 = move1.next
        # 翻转后半段链表
        with Reverselist(head=move1) as head_new: #O(n//2)
            move1.next = None
            move1 = self._head.next
            move2 = head_new
            while move1 is not None and head_new is not None: # O(n//2)
                head_new = move2.next
                move2.next = move1.next
                move1.next = move2
                move2 = head_new
                move1 = move1.next.next

    def __enter__(self):
        self.process()
        self.print(head=self._head.next)
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with ReorderList(nums=[1, 2, 3, 4]) as r1:
        pass
    with ReorderList(nums=[1, 2, 3, 4, 5]) as r2:
        pass
    with ReorderList(nums=[1, 2, 3, 4, 5, 6, 7]) as r3:
        pass