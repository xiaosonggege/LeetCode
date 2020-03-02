#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: __init__.py
@time: 2020/2/23 10:18 上午
'''
from collections import namedtuple, Counter
import copy

class BiTreeProperty:
    def __init__(self, name):
        self._name = '_' + name
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]
    def __set__(self, instance, value):
        instance.__dict__[self._name] = value

class BiTreesProperty:
    def __init__(self, name):
        self._name = '_' + name
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]
    def __set__(self, instance, value:tuple):
        value = list(value)
        stack = []
        stack.append(instance.__dict__[self._name])
        BiTreesProperty.build(value, stack)
    @staticmethod
    def build(value, stack):
        flag = 1
        if value[0] != 'None':
            stack[0].data = value.pop(0)
        for i in value:
            if i != 'None':
                if not stack[0].lchild and flag: #左子树为空
                    stack[0].lchild = BiTree(data=i)
                    stack.append(stack[0].lchild)
                elif not stack[0].rchild: #左子树非空，右子树为空
                    stack[0].rchild = BiTree(data=i)
                    stack.append(stack[0].rchild)
                    stack.pop(0) #父节点出队
                    flag = 1
            else:
                if stack[0].lchild: #左子树非空时若遇到None直接出队首位
                    stack.pop(0)
                else: #左子树为空时
                    flag = 0

class BiTree:
    def __init__(self, data=0, lchild=None, rchild=None):
        self._data = data
        self._lchild = lchild
        self._rchild = rchild

    data = BiTreeProperty('data')
    lchild = BiTreeProperty('lchild')
    rchild = BiTreeProperty('rchild')

class BiTrees:
    root = BiTreesProperty('root')
    def __init__(self):
        self._root = BiTree()
    def __call__(self, *args, **kwargs):
        self.root = args
        return self.root
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return True
    def __iter__(self):
        result = []
        def zhongxu(node):
            if node:
                if node.lchild:
                    zhongxu(node.lchild)
                result.append(node.data)
                if node.rchild:
                    zhongxu(node.rchild)
        zhongxu(self._root)
        return (i for i in result)
    def isSymmetric(self):
        def judge(nodel:BiTree, noder:BiTree):
            if not nodel and noder or nodel and not noder: # 如果两节点有一个为空，一个非空
                return 0
            elif not nodel and not noder: # 两个节点均为空
                return 1
            else: # 两节点均非空
                if nodel.data != noder.data: # 如果两节点均非空但值不一样
                    return 0
                else:  # 两节点值一样，则递归判断两节点的左子树和右子树
                    result = judge(nodel=nodel.lchild, noder=noder.rchild)
                    result *= judge(nodel=nodel.rchild, noder=noder.lchild)
                    return result

        return judge(self._root.lchild, self._root.rchild)


if __name__ == '__main__':
    # tree = BiTrees()
    lis = [1, 2, 2, 'None', 'None', 'None', 'None']
    with BiTrees() as tree:
        root = tree(*lis)
        import sys
        sys.stdout.write('中序遍历结果为:')
        for i in tree:
            print(i, end=' ')
        result = tree.isSymmetric()
        sys.stdout.write('\n是否为对称二叉树:')
        print(result)


