#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: isBalanced
@time: 2020/3/6 1:54 下午
'''
from No_101.__init__ import BiTree, BiTrees

class IsBalanced(BiTrees):
    def __init__(self):
        super().__init__()
        self._is_balance = True

    def _judge(self, node:BiTree)->int:
        lj = self._judge(node=node.lchild) if node.lchild else 0
        rj = self._judge(node=node.rchild) if node.rchild else 0
        self._is_balance = True if abs(lj - rj) <= 1 and self._is_balance else False
        return 1 + max(lj, rj)

    def __str__(self):
        self._judge(self._root)
        answer = 'yes' if self._is_balance else 'no'
        return answer


if __name__ == '__main__':
    lis = [1, 'None', 2, 3, 4, 4, 'None']
    with IsBalanced() as b:
        b(*lis)
        print(str(b))
