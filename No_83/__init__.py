#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: __init__.py
@time: 2020/2/21 5:06 下午
'''
import copy
import sys
class Pointproperty:
    def __init__(self, name):
        self._name = '_' + name
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]
    def __set__(self, instance, value):
        instance.__dict__[self._name] = value

class Point:
    def __init__(self, data=0, next=None):
        self._data = data
        self._next = next
    data = Pointproperty('data')
    next = Pointproperty('next')

class Lianbiao:
    def __init__(self):
        self._head = None
    def __call__(self, *args, **kwargs):
        self._build(datas=args)
        self._print()
        self._deleteDuplicates()
        print()
        self._print()

    def _build(self, datas:tuple)->None:
        datas_ = list(datas)
        self._head = Point(data=0)
        while len(datas_):
            temp = Point(datas_.pop())
            temp.next = self._head.next
            self._head.next = temp

    def _print(self):
        temp = self._head.next
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def _deleteDuplicates(self):
        temp = self._head.next
        while temp.next:
            temp2 = temp
            temp = temp.next
            if temp.data == temp2.data:
                temp2.next = temp.next
                temp = temp.next

if __name__ == '__main__':
    p = [1, 1, 2, 3, 4, 4, 5, 6, 6, 7]
    l = Lianbiao()
    l(*p)









