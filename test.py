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


class a:
    def __init__(self):
        self._b = 2
        self.c = 3
class b(a):
    def __init__(self):
        super(b, self).__init__()
        self._b = 3


if __name__ == '__main__':
    b = b()
    print(b._b)