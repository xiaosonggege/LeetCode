#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: test
@time: 2020/5/22 9:24 下午
'''

class Attri:
    def __init__(self, name):
        self._name = name
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]
    def __set__(self, instance, value):
        instance.__dict__[self._name] = value

class Name:
    x = Attri('y')
    def __init__(self):
        self.y = 3
    def __getattribute__(self, name):
        print(3)
        # self.__class__.__dict__['x'].__get__(self, self.__class__)
        super().__getattribute__(name)


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    try:
        pos = a.index(0)
    except ValueError:
        pos = -1
    print(pos)