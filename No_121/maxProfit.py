#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: maxProfit
@time: 2020/3/15 11:48 上午
'''

class MaxProfit:
    def __init__(self, *array):
        self._array = list(array)
        self._min = self._array.pop(0)
        self._max = self._min
        self._min_pre = self._min
        self._max_pre = self._min
        self._mp = 0 #最大收益
        self.calc = lambda min, max: max - min


    def __enter__(self):
        for i in self:
            self.maxprofit(value=i)
        return self._mp if self._mp >= self.calc(self._min, self._max) else self.calc(self._min, self._max)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if not self._array.__len__():
            raise StopIteration
        else:
            return self._array.pop(0)

    def maxprofit(self, value:int):
        if value > self._max:
            self._max = value
        elif value < self._min:
            mp_now = self.calc(self._min, self._max)
            if mp_now > self._mp:
                self._min_pre = self._min
                self._max_pre = self._max
                self._mp = mp_now

            self._min = value
            self._max = value

class Maxprofit2:
    def __init__(self, nums:list):
        self._nums = nums
        self._diff = [self._nums[i]-self._nums[i-1] for i in range(1, len(self._nums))]
        self._result = 0
    def maxprofit_fun2_sub(self, left, right)->int:
        mid = (left + right) // 2
        left_sum = 0
        right_sum = 0
        sum = self._diff[mid]
        for i in range(mid-1, left-1, -1):
            sum += self._diff[i]
            left_sum = max(left_sum, sum)
        sum = 0
        for i in range(mid+1, right+1):
            sum += self._diff[i]
            right_sum = max(right_sum, sum)
        return left_sum + right_sum

    def maxprofit_fun2(self, left, right): #O(nlogn)
        if left == right:
            return self.maxprofit_fun2_sub(left=left, right=right)
        else:
            mid = (left + right) // 2
            left_sum = self.maxprofit_fun2(left=left, right=max(left, mid-1))
            right_sum = self.maxprofit_fun2(left=min(mid+1, right), right=right)
            mid_sum = self.maxprofit_fun2_sub(left=left, right=right)
            return max(left_sum, mid_sum, right_sum)

if __name__ == '__main__':
    # with MaxProfit(7, 1, 5, 3, 6, 4) as m:
    #     print(m)
    #
    # with MaxProfit(7, 6, 4, 3, 1) as m:
    #     print(m)
    #
    # with MaxProfit(7, 3, 5, 8, 1, 4, 11) as m:
    #     print(m)

    m = Maxprofit2(nums=[7, 1, 5, 3, 6, 4])
    result = m.maxprofit_fun2(left=0, right=4)
    print(result)

