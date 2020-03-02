#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: __init__.py
@time: 2020/2/27 3:13 下午
'''
from No_101.__init__ import BiTrees, BiTree

class MaxDepth:
    def __init__(self, *args):
        self._maxdis = 0
        self._tree = BiTrees()
        self._tree.root = args
    def _maxdepth(self, node:BiTree)->int:
        if node:
            if node.lchild:
                left_depth = self._maxdepth(node.lchild)
            else:
                left_depth = 0
            if node.rchild:
                right_depth = self._maxdepth(node.rchild)
            else:
                right_depth = 0
            return max(left_depth, right_depth) + 1
    def __call__(self, *args, **kwargs):
        return self._maxdepth(self._tree.root)

if __name__ == '__main__':
    lis = [1, 2, 2, 'None', 4, 'None', 'None']
    m = MaxDepth(*lis)
    print(m())