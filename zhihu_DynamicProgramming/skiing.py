#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: skiing
@time: 2020/5/21 4:47 下午
'''
class Attri:
    def __init__(self, name):
        self._name = name
    def __get__(self, instance, owner):
        return instance.__dict__[self._name][instance.__dict__['_start'][0]][instance.__dict__['_start'][-1]]

class Skiing:
    final = Attri('_xuechang')
    def __init__(self):
        self._xuechang = [
            [1, 2, 3, 4, 5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9]
        ]
        self._len = self._xuechang.__len__()
        #存储各点为终点的最长路径
        self._max_route = [[0] * self._len for _ in range(self._len)]
        #记录各个位置是否已获知以各点为终点的最长路径长度
        self._flag = [[0] * self._len for _ in range(self._len)]
        self._start = 2, 2

    def sking(self, point:tuple):
        max_route = 0
        if self._flag[point[0]][point[-1]] == 0: #还未得到
            if point[0] > 0 and self._xuechang[point[0]-1][point[-1]] < self._xuechang[point[0]][point[-1]]:
                max_route = max(max_route, self.sking(point=(point[0]-1,point[-1])))
            if point[0] < self._len - 1 and self._xuechang[point[0]+1][point[-1]] < self._xuechang[point[0]][point[-1]]:
                max_route = max(max_route, self.sking(point=(point[0]+1,point[-1])))
            if point[-1] > 0 and self._xuechang[point[0]][point[-1]-1] < self._xuechang[point[0]][point[-1]]:
                max_route = max(max_route, self.sking(point=(point[0], point[-1]-1)))
            if point[-1] < self._len - 1 and self._xuechang[point[0]][point[-1]+1] < self._xuechang[point[0]][point[-1]]:
                max_route = max(max_route, self.sking(point=(point[0], point[-1]+1)))
            self._flag[point[0]][point[-1]] = 1
            self._max_route[point[0]][point[-1]] = max_route + 1

        return self._max_route[point[0]][point[-1]]

    def __enter__(self):
        max_route = self.sking(point=self._start)
        return max_route
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with Skiing() as s:
        print(s)