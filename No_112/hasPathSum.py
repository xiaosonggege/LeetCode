#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: hasPathSum
@time: 2020/3/9 2:23 下午
'''
from No_101.__init__ import BiTrees, BiTree
class HasPathSumProperty:
    def __init__(self, name):
        self._name = '_' + name
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]
    def __set__(self, instance, value):
        instance.__dict__[self._name] = value

class HasPathSum(BiTrees):
    def __init__(self, objectvalue):
        super().__init__()
        self._objectvalue = objectvalue
    objectvalue = HasPathSumProperty('objectvalue')

    def _judge(self, node:BiTree, objectvalue:int):
        if not node:
            print('no')
        else:
            if node.data > objectvalue:
                print('no')
            elif node.data == objectvalue:
                print('yes')
            else:
                self._judge(node.lchild, objectvalue=objectvalue-node.data)
                self._judge(node.rchild, objectvalue=objectvalue-node.data)

    def __call__(self, *args, **kwargs):
        self.root = args
        self._judge(node=self.root, objectvalue=self.objectvalue)


if __name__ == '__main__':
    lis = [1, 2, 2, 3, 4, 4, 3]
    with HasPathSum(6) as h:
        h(*lis)
