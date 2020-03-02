#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: __init__.py
@time: 2020/2/20 5:03 下午
'''
import copy

class Property:
    def __init__(self, name):
        self._name = '_' + name
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]
    def __set__(self, instance, value):
        instance.__dict__[self._name] = value

class ClimbStairs:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True

    def __init__(self, s1:int=1, s2:int=2, input:int=3)->None:
        self._s1 = s1
        self._s2 = s2
        self._input = input
        self._output = 0
    input = Property('input')
    output = Property('output')
    def __call__(self, *args, **kwargs):
        self._climb()

    def _climb(self, mul=0):
        if mul + self._s1 < self._input:
            self._climb(mul+self._s1)
        elif mul + self._s1 == self._input:
            self._output += 1
        if mul+ self._s2 < self._input:
            self._climb(mul+self._s2)
        elif mul + self._s2 == self._input:
            self._output += 1


if __name__ == '__main__':
    try:
        with ClimbStairs() as c:
            c.input = 6
            c()
            print(c.output)
    except Exception:
        print('error!')

