#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: trailingZeroes
@time: 2020/5/11 11:23 上午
'''


class TrailingZeroes:
    def __init__(self, n:int)->None:
        self._n = n
        self._n5 = 0
        self._n2 = 0

    def testTwo(self, n:int)->None:
        if n >= 2 and n % 2 == 0:
            self._n2 += 1
            self.testTwo(n//2)

    def testFive(self, n:int)->None:
        if n % 5 == 0:
            self._n5 += 1
            self.testFive(n // 5)
        else:
            self.testTwo(n)

    def logn_function(self, n:int)->int:
        if n:
            return n // 5 + self.logn_function(n // 5)
        else:
            return 0

    def __enter__(self):
        # for n in range(self._n, 0, -1):
        #     self.testFive(n)
        self._n5 = self.logn_function(self._n)
        return self._n5

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with TrailingZeroes(5) as result:
        print(result)
    with TrailingZeroes(6) as result:
        print(result)
    with TrailingZeroes(10) as result:
        print(result)
    with TrailingZeroes(15) as result:
        print(result)
    with TrailingZeroes(20) as result:
        print(result)