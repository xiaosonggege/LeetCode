#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: getIntersectionNode
@time: 2020/5/7 9:05 上午
'''
from No_141.hasCycle import ListNode
class GetIntersectionNode:
    def __init__(self, listA:list, skipA:int, listB:list, skipB:int):
        self._headA, self._headB = self._create(listA, listB, skipA, skipB)
        self._len_total = listA.__len__() + listB.__len__()

    def _create(self, listA:list, listB:list, skipA:int, skipB:int)->tuple:
        headA = moveA = ListNode(val=-1)
        headB = moveB = ListNode(val=-1)
        intersectionnode = None
        flag = 0
        for i in listA:
            moveA._replace(next=ListNode(val=i, next=moveA.next))
            moveA = moveA.next
            flag += 1
            if flag == skipA+1:
                intersectionnode = moveA
        flag = 0
        for i in listB:
            flag += 1
            if skipB+1 == flag:
                moveB._replace(next=intersectionnode)
                break
            else:
                moveB._replace(next=ListNode(val=i, next=moveB.next))
                moveB = moveB.next
        return headA, headB

    def IntersectionNode(self)->int:
        moveA, moveB = self._headA, self._headB
        time = 0
        # print(self._len_total)
        while time <= self._len_total:
            moveA = moveA.next if moveA.next is not None else self._headB.next
            moveB = moveB.next if moveB.next is not None else self._headA.next
            time += 1
            if id(moveA) == id(moveB):
                return moveA.val
        else:
            return 0


    def __enter__(self):
        i = self.IntersectionNode()
        print(i)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with GetIntersectionNode(listA=[4, 1, 8, 4, 5], listB=[5, 0, 1, 8, 4, 5], skipA=2, skipB=3) as g1:
        pass

    with GetIntersectionNode(listA=[0, 9, 1, 2, 4], listB=[3, 2, 4], skipA=3, skipB=1) as g2:
        pass

    with GetIntersectionNode(listA=[2, 6, 4], listB=[1, 5], skipA=3, skipB=2) as g3:
        pass
