#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: fast_sort
@time: 2020/6/26 3:32 下午
'''

class Fastsort:
    def __init__(self, nums:list):
        self._nums = nums

    def single_operation(self, p=-1, r=-1)->int:
        '''
        :param p:首地址
        :param r:尾地址
        '''
        i, j = p, p + 1
        while j <= len(self._nums)-2: # O(n)
            if self._nums[j] < self._nums[r]:
                i += 1
                if i != j:
                    self._nums[i], self._nums[j] = self._nums[j], self._nums[i]
            j += 1
        self._nums[i+1], self._nums[r] = self._nums[r], self._nums[i+1]
        return i + 1

    def __enter__(self):
        self.single_operation()
        return
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with Fastsort(nums=[4, 6, 3, 2, 6, 5]) as f1:
        pass