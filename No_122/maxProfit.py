#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: maxProfit
@time: 2020/6/12 7:16 下午
'''

class MaxProfit:
    def __init__(self, prices:list):
        self._prices = prices
        self._max_money = 0

    def process(self):
        price_diff = []
        for i in range(1, len(self._prices)): # O(n-1)
            price_diff.append(self._prices[i] - self._prices[i-1])
        for i in range(len(price_diff)): # O(n-1)
            if self._max_money < self._max_money + price_diff[i]:
                self._max_money += price_diff[i]

    def __enter__(self):
        self.process()
        return self._max_money
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with MaxProfit(prices=[7, 1, 5, 3, 6, 4]) as m1:
        print(m1)
    with MaxProfit(prices=[7, 6, 8, 5, 4, 3, 9]) as m2:
        print(m2)