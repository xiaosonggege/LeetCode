#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: threeSumClosest
@time: 2020/6/13 4:02 下午
'''


class ThreeSumClosest:
    def __init__(self, nums:list, target:int):
        self._nums = nums
        self._target = target
        self._group = 0
        self._pos = None

    def process(self):
        nums_sort = sorted(self._nums) #O(nlogn)
        self._min_dis = 100 #最小距离初始化
        for i in range(len(nums_sort)-2): #O(n^2)
            left = i + 1
            right = len(nums_sort) - 1
            while left < right:
                if nums_sort[left] == nums_sort[left+1]:
                    left += 1
                if nums_sort[right] == nums_sort[right-1]:
                    right -= 1
                result1 = nums_sort[i] + nums_sort[left] + nums_sort[right]
                result2 = abs(result1 - self._target)
                if self._min_dis > result2:
                    self._min_dis = result2
                    self._group = result1
                    self._pos = [i, left, right]
                if result1 < self._target:
                    left += 1
                elif result1 > self._target:
                    right -= 1
                else:
                    break
    def __enter__(self):
        self.process()
        return self._group, self._pos
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with ThreeSumClosest(nums=[2, -3, 8, 5, -6], target=3) as t1:
        print(t1)
    with ThreeSumClosest(nums=[-1, 2, 1, -4], target=1) as t2:
        print(t2)