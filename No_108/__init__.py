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
import copy
class Sproperty:
    def __init__(self, name):
        self._name = '_' + name
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]
    def __set__(self, instance, value):
        instance.__dict__[self._name] = BiTree(data=value)

class SortedArrayToBST():
    def __init__(self, array):
        self._array = array
        self._root = None
    root = Sproperty('root')

    def _buildtree(self):
        array = copy.deepcopy(self._array)
        while len(array):
            if not self.root:
                self.root = array.pop(0)
            else:
                point = self.root
                assert isinstance(point, BiTree)
                while True:
                    if array[0] <= point.data:
                        if not point.lchild:
                            point.lchild = BiTree(data=array.pop(0))
                            break
                        else:
                            point = point.lchild
                    else:
                        if not point.rchild:
                            point.rchild = BiTree(data=array.pop(0))
                            break
                        else:
                            point = point.rchild

    def __call__(self, *args, **kwargs):
        self._buildtree()
    # def __enter__(self):
    #     return self
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     return True

if __name__ == '__main__':
    l1 = [0, -3, -1, -10, 5, 9]
    s = SortedArrayToBST(l1)
    s()
    print()
    with SortedArrayToBST(l1) as s1:
        s1()
