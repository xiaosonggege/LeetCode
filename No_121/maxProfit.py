#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: maxProfit
@time: 2020/3/15 11:48 上午
'''

class maxProfit:
    def __init__(self, *array):
        self._array = list(array)
        self._min = self._array.pop(0)
        self._max = self._min
        self._min_pre = self._min
        self._max_pre = self._min
        self._mp = 0 #最大收益
        self.calc = lambda min, max: max - min

    def __enter__(self):
        for i in self:
            self.maxprofit(value=i)
        return self._mp if self._mp >= self.calc(self._min, self._max) else self.calc(self._min, self._max)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if not self._array.__len__():
            raise StopIteration
        else:
            return self._array.pop(0)

    def maxprofit(self, value:int):
        if value > self._max:
            self._max = value
        elif value < self._min:
            mp_now = self.calc(self._min, self._max)
            if mp_now > self._mp:
                self._min_pre = self._min
                self._max_pre = self._max
                self._mp = mp_now

            self._min = value
            self._max = value


if __name__ == '__main__':
    with maxProfit(7, 1, 5, 3, 6, 4) as m:
        print(m)

    with maxProfit(7, 6, 4, 3, 1) as m:
        print(m)

    with maxProfit(7, 3, 5, 8, 1, 4, 11) as m:
        print(m)

