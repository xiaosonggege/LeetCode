#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: __init__.py
@time: 2020/3/4 3:11 下午
'''
import numpy as np
class FinderProperty:
    def __init__(self, name):
        self._name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value

class Finder:
    def __init__(self, graph=None, start_point=(0, 0)):
        self._graph = graph
        self._start_point = start_point
    graph = FinderProperty('graph')
    start_point = FinderProperty('start_point')

    def _DFS(self, stack, pos):
        if stack is None:
            stack = [self._start_point]
        else:
            stack.append(pos)
        if self._graph[pos[0], pos[1]] == self._graph[self._start_point[0], self._start_point[1]]:
            print(pos)
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if abs(i) != abs(j):
                    if pos[0]+i>=0 and pos[0]+i<self._graph.shape[0] and pos[1]+j>=0 and pos[1]+j <self._graph.shape[-1] \
                            and (pos[0]+i, pos[-1]+j) not in stack:
                        self._DFS(stack=stack, pos=(pos[0]+i, pos[-1]+j))

    def __call__(self, *args, **kwargs):
        self._DFS(stack=[], pos=self._start_point)


if __name__ == '__main__':
    graph = np.array(
        [[0, 1, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 0]])
    f = Finder(graph=graph, start_point=(3, 2))
    f()