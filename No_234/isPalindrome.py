#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: isPalindrome
@time: 2020/6/15 11:18 上午
'''
from No_24.ReverseList import Node, Linked, Reverselist
class IsPalindrome(Linked):
    def __init__(self, nums:list, head:Node=None):
        super().__init__(nums=nums)
        self._flag = 1 #表示是否是回文
        self._head = self.create()

    def judge(self): #O(n/2+n/2+n/2)=O(3n/2)=O(n)
        move_fast = self._head
        move_slow = self._head
        while move_fast.next is not None: #O(n/2)
            move_fast = move_fast.next.next
            move_slow = move_slow.next
            if move_fast is None:
                break
        move = self._head.next
        with Reverselist(head=move_slow) as head_new: #O(n/2)
            while head_new is not None: #O(n/2)
                if head_new.value != move.value:
                    self._flag = 0
                    break
                head_new = head_new.next
                move = move.next

    def __enter__(self):
        self.judge()
        return self._flag
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with IsPalindrome(nums=[1, 2, 2, 1]) as i:
        print('is:%s' % i)
    with IsPalindrome(nums=[1, 2, 3, 4, 4, 3, 2, 1]) as i2:
        print('is:%s' % i2)
    with IsPalindrome(nums=[1, 2, 3, 2, 1]) as i3:
        print('is:%s' % i3)
    with IsPalindrome(nums=[1, 2, 3, 4, 1]) as i4:
        print('is:%s' % i4)