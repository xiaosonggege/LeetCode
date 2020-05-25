#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: jiemugun
@time: 2020/5/22 11:47 下午
'''

class Qiebangzi:
    def __init__(self, L:int, lengths:list, prices:list):
        self._L = L
        self._lengths = lengths
        self._prices = prices
        #最大收益向量,设总共截取长度为0时的收益是0
        self._max_price = [0]*self._L

    def dp_321(self, n:int):
        '''
        顺序递推
        '''
        total_price_temp = 0
        for i in range(self._lengths.__len__()):
            if n - self._lengths[i] >= 0:
                total_price_temp = max(total_price_temp, self._prices[i] + self.dp_321(n=n - self._lengths[i]))
            else:
                break

        return total_price_temp

if __name__ == '__main__':
    q = Qiebangzi(L=23, lengths=[i for i in range(1, 11)], prices=[1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
    print(q.dp_321(q._L))