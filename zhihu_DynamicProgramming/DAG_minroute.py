#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: DAG_minroute
@time: 2020/5/20 3:49 下午
'''

class DAG_min:
    def __init__(self):
        self._linjie_martix = [
            [0, 0, 30, 10, 0, 0],
            [0, 0, 0, 20, 0, 0],
            [0, 0, 0, 5, 0, 20],
            [0, 0, 0, 0, 0, 10],
            [10, 20, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]
        #记录各点到T的最短路径,初始化为最大权值,并且T点的最短路径为0
        self._f_point = [30] * (self._linjie_martix.__len__()-1) + [0] #记录各点到T的最短路径,初始化为最大权值
        self._nums_point = self._linjie_martix.__len__()
        self._rank = [self._nums_point-1] #临时存储栈

    def find_min_route(self):
        if self._rank.__len__():
            for i in range(self._nums_point):
                weight = self._linjie_martix[i][self._rank[0]]
                if weight != 0:
                    self._rank.append(i)
                    self._f_point[i] = min(self._f_point[i], weight + self._f_point[self._rank[0]])
            self._rank.pop(0)
            self.find_min_route()

    def min_route(self):
        self.find_min_route()
        return self._f_point

if __name__ == '__main__':
    d = DAG_min()
    print(d.min_route())