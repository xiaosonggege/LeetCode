#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: test
@time: 2020/6/25 9:45 上午
'''
from collections.abc import Iterable, Iterator, Generator, Callable

def fun1(fun2):
    fun2()
    return fun2
class A:
    def __init__(self):
        self._a = 4
        self._flag = 10

    @staticmethod
    # @fun1
    def fun2():
        a = 3
        c = 4
        print(3)

    def __enter__(self):
        try:
            if self._a == 1:
                raise StopIteration('woaixing')
        except StopIteration as s:
            print(s.value)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type ==  StopIteration:
            print('song')
        if exc_type == KeyError:
            print(exc_val.__str__())
        return True
    e = 5
    def __getattribute__(self, item):
        print('ai')

def fun4():
    e = 4
    f = []
    def fun3():
        # global e
        f.append(5)
        e = 4
    return fun3

if __name__ == '__main__':
    a = A()
    a.x = 3
    print(a.__dict__, A.__dict__)
    print(a.__getattribute__ == A.__getattribute__)

