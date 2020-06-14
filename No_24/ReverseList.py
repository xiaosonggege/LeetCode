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
    def __init__(self, nums:list):
        self._nums = nums
        self._head = Node(value=None)

    def print(self, head):
        m = head
        while m is not None:
            print(m.value)
            m = m.next
    def create(self):
        for i in reversed(self._nums):
            m = Node(value=i, next=self._head.next)
            self._head.next = m
        return self._head

class Reverselist(Linked):
    def __init__(self, head:Node=None, nums:list=None):
        super().__init__(nums=nums)
        # self._head = head
        self._head_new = None
        self._head = self.create()
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
        self.print(head=self._head_new)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':
    with Reverselist(nums=[1, 2, 3, 4, 5]) as r1:
        pass

