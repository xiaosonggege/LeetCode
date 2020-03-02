#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: mySqrt
@time: 2020/2/20 3:33 下午
'''
import numpy as np

class MySqrt:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == StopIteration:
            print('精度已经达到!')
            import traceback
            print(traceback.extract_tb(tb=exc_tb))
            return True

    def __init__(self, number):
        self._number = number
        self._val = number
        self._val_ = self._val + 1
        self._fun = lambda x: (x + self._number / x) / 2

    def __iter__(self):
        return self

    def __next__(self):
        if np.abs(self._val - self._val_) < 1e-6:
            raise StopIteration
        else:
            self._val_ = self._val
            self._val = self._fun(self._val)
            return self._val

if __name__ == '__main__':
    with MySqrt(2) as m:
        while True:
            val = next(m)
            print(val)


