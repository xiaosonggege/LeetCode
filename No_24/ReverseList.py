#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: ReverseList
@time: 2020/6/13 7:56 下午
'''
class Node:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, val):
        self._value = val

    @property
    def next(self):
        return self._next
    @next.setter
    def next(self, val):
        self._next = val

class Linked:
    def __init__(self, nums:list=None):
        self._nums = nums
        self._head = Node(value=None)

    def print(self, head):
        m = head
        count = 0
        while m is not None and count < 2 * len(self._nums):
            print(m.value, end=' ')
            m = m.next
            count += 1
        print()
    def create(self, end:int=None):
        '''
        end为尾结点地址，建立循环链表时使用
        '''
        if end is not None:
            pos = 0
            end_node = None
        for i in reversed(self._nums):
            m = Node(value=i, next=self._head.next)
            if end is not None:
                if pos == 0:
                    end_node = m
                    pos += 1
                elif len(self._nums) - pos > end + 1:
                    pos += 1
                elif len(self._nums) - pos == end + 1:
                    end_node.next = m
                    pos += 1
            self._head.next = m
        return self._head

class Reverselist(Linked):
    def __init__(self, head:Node=None, nums:list=None):
        super().__init__(nums=nums)
        # self._head = head
        self._head_new = None
        self._head = head if head is not None else self.create()
    def reverse(self):
        if self._head is not None:
            move1 = self._head.next
            move3 = move1
            move2 = move1.next
            while move2 is not None: #O(n)
                move1.next = move2.next
                move2.next = move3
                move3 = move2
                move2 = move1.next
            self._head_new = move3

    def __enter__(self):
        self.reverse()
        # self.print(head=self._head_new)
        return self._head_new
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':
    with Reverselist(nums=[1, 2, 3, 4, 5]) as r1:
        pass

