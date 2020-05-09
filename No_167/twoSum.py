#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: twoSum
@time: 2020/5/8 10:54 上午
'''
import copy
class TwoSum:
    def __init__(self, numbers:list, target:int):
        self._numbers = copy.deepcopy(numbers)
        self._target = target / 2

    def _postion_ensure(self, low:int, high:int)->int:
        mid = (low + high) // 2
        if self._target < self._numbers[mid]:
            return self._postion_ensure(low=low, high=mid)
        elif self._target > self._numbers[mid]:
            if self._target < self._numbers[mid+1]:
                return mid
            else:
                return self._postion_ensure(low=mid, high=high)

    def _sumEnsure(self)->tuple:
        left = self._postion_ensure(low=0, high=len(self._numbers)-1)
        # print('left:{0}'.format(left))
        right = left + 1
        sum = -1
        while (sum != self._target * 2):
            sum = self._numbers[left] + self._numbers[right]
            if sum > self._target * 2:
                if left - 1 >= 0:
                    left -= 1
                else:
                    return -1, -1
            elif sum < self._target * 2:
                if right + 1 < len(self._numbers) - 1:
                    right += 1
                else:
                    return -1, -1
            else:
                return (self._numbers[left], self._numbers[right])

    def __enter__(self):
        left, right = self._sumEnsure()
        return left, right
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with TwoSum(numbers=[2, 7, 11, 15, 17, 19, 21], target=9) as t:
        print(t)
    with TwoSum(numbers=[2, 7, 11, 15, 17, 19, 21], target=28) as t:
        print(t)
    with TwoSum(numbers=[2, 7, 11, 15, 17, 19, 21], target=32) as t:
        print(t)