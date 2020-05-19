#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: rob
@time: 2020/5/18 12:35 上午
'''

class Rob:
    def __init__(self, nums:list)->None:
        self._nums = nums
        self._f = 0
        self._f_1 = 0
        self._f_2 = 0
    def rob(self):
        for i in self._nums:
            self._f_2 = self._f_1
            self._f_1 = self._f
            self._f = max(self._f_1, i + self._f_2)
        return self._f

    def __enter__(self):
        return self.rob()
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with Rob([1,2,3,1]) as r:
        print(r)
    with Rob([2, 7, 9, 3, 1]) as r:
        print(r)
    with Rob([4, 1, 2, 7, 8, 3, 1, 6]) as r:
        print(r)