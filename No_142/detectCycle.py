#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: detectCycle
@time: 2020/6/18 10:29 上午
'''
from No_24.ReverseList import Node, Linked
class DetectCycle:
    def __init__(self, head:Node=None, nums:list=None, pos:int=None):
        l = Linked(nums=nums)
        self._head = l.create(end=pos)
        # l.print(head=self._head)

    def find(self): #时间复杂度为O(n),空间复杂度为O(n)
        move = self._head.next
        data_dict = {}
        count = 1
        cycle_start = -1
        while move is not None and cycle_start == -1:
            indice = data_dict.setdefault(id(move), count)
            if indice < count: #如果索引在散列表中出现过
                cycle_start =  indice #返回循环起始点
            move = move.next
            count += 1
        return cycle_start

    def double_point(self): #时间复杂度O(n) 空间复杂度O(1)
        move1 = move2 = self._head
        move3 = None
        flag = 0 #慢指针移动标志
        cycle = -1
        # 记录快慢指针第一次相遇位置
        while (move1 != move2 or flag == 1) or move1 == move2 == self._head:
            if move2 is None:
                break
            move2 = move2.next
            if flag == 1:
                move1 = move1.next
            flag = 1 - flag
        # 记录快慢指针第一次相遇的位置
        if move1 == move2:
            move3 = move1
            move1 = self._head
            count = 0
            while move1 != move3:
                move1 = move1.next
                move3 = move3.next
                count += 1
            cycle = count
        return cycle #环形链表起始点位置,-1代表无环

    def __enter__(self):
        # cycle_start = self.find()
        cycle_start = self.double_point()
        return cycle_start
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with DetectCycle(nums=[1, 2, 3, 4], pos=1) as d1:
        print(d1)
    with DetectCycle(nums=[1, 2, 3, 4, 5, 6], pos=2) as d2:
        print(d2)
    with DetectCycle(nums=[1, 2, 3, 4]) as d3:
        print(d3)