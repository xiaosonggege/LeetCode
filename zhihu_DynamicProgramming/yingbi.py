#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: addTwoNumbers
@time: 2020/5/19 4:21 下午
'''

class Yingbi:
    def __init__(self, money:int):
        self._need_money = money
        self._money1 = 1
        self._money2 = 5
        self._money3 = 11
        self._min_num = [0]

    def process(self):
        n = 1
        while n != self._need_money:
            cost = self._need_money + 10
            if n - 1 >= 0:
                cost = min(cost, self._min_num[n - 1]+1)
            if n - 5 >= 0:
                cost = min(cost, self._min_num[n - 5]+1)
            if n - 11 >= 0:
                cost = min(cost, self._min_num[n - 11]+1)
            self._min_num.append(cost)
            n += 1
            # print(self._min_num[n-1])
        return min(self._min_num[n-1], self._min_num[n-5], self._min_num[n-11]) + 1

if __name__ == '__main__':
    y = Yingbi(money=15)
    print(y.process())