#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: __init__.py
@time: 2020/2/22 2:36 下午
'''
import copy
class Merg:
    def __init__(self, lis1:list, lis2:list):
        self._lis1 = copy.deepcopy(lis1)
        self._lis2 = copy.deepcopy(lis2)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._lis1) and len(self._lis2):
            if self._lis1[0] <= self._lis2[0]:
                return self._lis1.pop(0)
            else:
                return self._lis2.pop(0)
        elif not len(self._lis1) and not len(self._lis2):
            raise StopIteration
        else:
            if len(self._lis1):
                return self._lis1.pop(0)
            else:
                return self._lis2.pop(0)
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == Exception:
            print('exit')
            return True


if __name__ == '__main__':
    lis1 = [1, 2, 3, 5]
    lis2 = [2, 5, 6]
    with Merg(lis1=lis1, lis2=lis2) as m:
        for i in m:
            print(i)
        raise Exception