#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: maxSubArray
@time: 2020/2/17 11:23 上午
'''
class MaxSubArray:
    def __init__(self):
        """
        构造函数
        """
        self._array = [-2,-1,-3,-4,-1,-2,-1,-5,-4] #[-2,1,-3,4,-1,2,1,-5,4]
        self._result = self._array[0]


    def dongtaiguihua(self):
        sum = self._array[0]
        for i in self._array:
            if sum < 0:
                sum = i
            else:
                sum += i
            self._result = max(self._result, sum)

    def tanxin(self):
        sum = 0
        for i in self._array:
            sum += i
            self._result = max(self._result, sum)
            if sum < 0:
                sum = 0

    @property
    def result(self):
        return self._result

if __name__ == '__main__':
    m = MaxSubArray()
    # m.dongtaiguihua()
    m.tanxin()
    print(m.result)