#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: LIS
@time: 2020/5/21 11:10 上午
'''

class MaxLengthSubSquence:
    def __init__(self, nums:list):
        self._nums = nums
        #存储各个点处的最长递增子序列
        self._max_length_nums = [1] + [0] * (self._nums.__len__()-1)
        self._max_length = 0

    def function1(self):
        i = 1
        while i < self._nums.__len__():
            if self._nums[i] >= self._nums[i-1]:
                self._max_length_nums[i] = 1 + self._max_length_nums[i-1]
            else:
                j = i - 1
                while j >= 0 and self._nums[i] < self._nums[j]:
                    j -= 1
                self._max_length_nums[i] = 1 + self._max_length_nums[j]
            self._max_length = max(self._max_length, self._max_length_nums[i])
            i += 1
        return self._max_length, self._max_length_nums

    def function2(self):
        pass

if __name__ == '__main__':
    m = MaxLengthSubSquence([1, 5, 3, 4, 6, 9, 7, 8])
    print(m.function1())