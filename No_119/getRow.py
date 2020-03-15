#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: getRow
@time: 2020/3/13 9:59 下午
'''
import copy
import numpy as np
class GetrowProperty:
    def __init__(self, name):
        self._name = '_' + name
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]
    def __set__(self, instance, value):
        instance.__dict__[self._name] = value

class GetRow:
    def __init__(self, num):
        self._num = num
        self._lis = [1]
    num = GetrowProperty('num')
    def _yanghui(self):
        if not (self._num-1):
            return self._lis
        else:
            self._lis = np.array([0] + self._lis) + np.array(copy.deepcopy(self._lis) + [0])
            self._lis = self._lis.tolist()
            self._num -= 1
            return self._yanghui()
    def __call__(self, *args, **kwargs):
        return self._yanghui()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == AssertionError:
            print('你是')
        print(exc_type, exc_val)
        return True



if __name__ == '__main__':
    with GetRow(5) as g:
        print(g())
        assert len(g()) > 10, "我是🐷"
