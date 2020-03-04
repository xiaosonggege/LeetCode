#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: __init__.py
@time: 2020/2/29 10:18 下午
'''
from No_101.__init__ import BiTrees, BiTree
# import copy

class SortedArrayToBST(BiTrees):
    def __init__(self, array):
        super(SortedArrayToBST, self).__init__()
        self._array = array
    def _buildtree(self):
        array = copy.deepcopy(self._array)
        while len(array):
            if not self.root:
                self.root = BiTree(data=self._array.pop(0))
            else:
                point = self.root
                while True:
                    if self._array[0] <= point.data:
                        if not point.lchild:
                            point.lchild = BiTree(data=self._array.pop(0))
                            break
                        else:
                            point = point.lchild
                    else:
                        if not point.rchild:
                            point.rchild = BiTree(data=self._array.pop(0))
                            break
                        else:
                            point = point.rchild

    def __call__(self, *args, **kwargs):
        self._buildtree()

if __name__ == '__main__':
    l1 = [-10, -3, 0, 5, 9]
    for i in SortedArrayToBST(l1)():
        print(i)