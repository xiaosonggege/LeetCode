#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: quanpailie
@time: 2020/2/28 2:10 下午
'''
import copy

class Aproperty:
    def __init__(self, name):
        self._name = '_' + name
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]
    def __set__(self, instance, value):
        instance.__dict__[self._name] = value

class A:
    """全排列"""
    def __init__(self, lis=None):
        self._list = lis
        self._result = []
    lis = Aproperty('list')
    def _quanpailie(self, lis, index=0):
        for i in range(index, len(lis)):
            lis[index], lis[i] = lis[i], lis[index]
            if index != len(self._list)-1:
                self._quanpailie(lis, index+1)
            else:
                self._result.append(copy.deepcopy(lis))
            lis[index], lis[i] = lis[i], lis[index]
    def __call__(self, *args, **kwargs):
        self._quanpailie(self._list)
        return self._result
    def __iter__(self):
        self._quanpailie(self._list)
        return (i for i in self._result)
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return True

if __name__ == '__main__':
    l = [1, 2, 3, 4]
    with A(l) as a:
        for i in a:
            print(i)
