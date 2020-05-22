#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: tortoise_chess
@time: 2020/5/22 3:37 下午
'''
from collections import Counter

class Tortoise_chess:
    def __init__(self, N:int, M:int, scores:list, steps:list):
        self._N = N #格子数
        self._M = M #牌子数
        self._scores = scores
        self._steps = steps
        self._per_step = Counter(self._steps) #不同牌子的数量
        #n维数组构造f(n)
        self._f_n = [[[0]*(self._per_step[3]+1) for _ in range(self._per_step[2]+1)] for _ in range(self._per_step[1]+1)]

    def dp(self):
        for a in range(self._per_step[1]+1):
            for b in range(self._per_step[2]+1):
                for c in range(self._per_step[3]+1):
                    if a:
                        self._f_n[a][b][c] = max(self._f_n[a][b][c], self._f_n[a - 1][b][c])
                    if b:
                        self._f_n[a][b][c] = max(self._f_n[a][b][c], self._f_n[a][b - 1][c])
                    if c:
                        self._f_n[a][b][c] = max(self._f_n[a][b][c], self._f_n[a][b][c - 1])
                    self._f_n[a][b][c] += self._scores[1 * a + 2 * b + 3 * c]
        return self._f_n[self._per_step[1]][self._per_step[2]][self._per_step[3]]

if __name__ == '__main__':
    t = Tortoise_chess(N=9, M=5, scores=[6, 10, 14, 2, 8, 8, 18, 5, 17], steps=[1, 3, 1, 2, 1])
    print(t.dp())