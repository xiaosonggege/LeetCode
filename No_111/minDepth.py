#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: minDepth
@time: 2020/3/6 2:38 下午
'''
from No_101.__init__ import BiTrees, BiTree

class MinDepth(BiTrees):
    def __init__(self):
        super().__init__()
        self._len = True

    def _judge(self, node: BiTree) -> int:
        lj = self._judge(node=node.lchild) if node.lchild else 0
        rj = self._judge(node=node.rchild) if node.rchild else 0
        return 1 + min(lj, rj)

    def __str__(self):
        self._len = self._judge(self._root)
        answer = str(self._len)
        return answer


if __name__ == '__main__':
    lis = [1, 2, 2, 3, 4, 4, 3]
    with MinDepth() as b:
        b(*lis)
        print(str(b))