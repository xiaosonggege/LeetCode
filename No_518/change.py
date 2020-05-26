#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: change
@time: 2020/5/25 10:19 下午
'''
import copy
class Change:
    def __init__(self, amount:int, coins:list):
        self._amount = amount
        self._coins = coins
        self._combining_num = [1] + [0] * self._amount
    def finding(self):
        for coin in self._coins:
            for i in range(coin, self._combining_num.__len__()):
                self._combining_num[i] += self._combining_num[i-coin]
        return self._combining_num[-1]

    def __enter__(self):
        result = self.finding()
        return result

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with Change(amount=5, coins=[1, 2, 5]) as r1:
        print(r1)
    with Change(amount=5, coins=[3, 4]) as r2:
        print(r2)