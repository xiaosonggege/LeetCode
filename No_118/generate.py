#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: generate
@time: 2020/3/13 5:26 下午
'''
import copy
import numpy as np

class Generate:
    def __init__(self, retrain:int):
        self._retrain = retrain
        self._flag = 0
        self._row = [1]
    def __iter__(self):
        return self
    def __next__(self):
        if not self._flag :
            self._flag += 1
            return self._row
        else:
            lis = np.array(copy.deepcopy(self._row) + [0])
            self._row = (np.array([0] + self._row) + lis).tolist()
            if self._flag == self._retrain:
                raise StopIteration
            self._flag += 1
            return self._row
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return True

if __name__ == '__main__':
    with Generate(9) as g:
        for i in g:
            print(i)

