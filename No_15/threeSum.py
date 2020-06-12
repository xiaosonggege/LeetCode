#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: threeSum
@time: 2020/6/9 4:10 下午
'''
import _bisect
class ThreeSum:
    def __init__(self, nums:list, value:int):
        self._nums = nums
        self._value = value
        self._result = set()

    def two_finding(self): #两个配对儿
        nums_dict = dict()
        for i in self._nums:
            if nums_dict.get(i) is None:
                nums_dict[self._value - i] = i
            else:
                self._result.add((i, nums_dict[i]))

    def three_finding(self): #三个配对儿, O(n^2)
        # 排序
        nums_sort = sorted(self._nums) # O(nlogn)
        for i in range(len(nums_sort)-2): #保证有最少三个元素可以相加, O(n^2)
            dict_nums = {}
            for j in range(i+1, len(nums_sort)): # O(n-1)
                if dict_nums.get(nums_sort[j]) is None:
                    dict_nums[self._value-nums_sort[i]-nums_sort[j]] = nums_sort[j]
                else:
                    self._result.add(tuple(sorted([nums_sort[i], nums_sort[j], self._value-nums_sort[i]-nums_sort[j]])))

    def three_finding_double_point(self): #三个配对儿，双指针法, O(n^2)
        if self._nums.__len__() < 3:
            return
        else:
            #排序
            nums_sort = sorted(self._nums) # O(nlogn)
            if nums_sort[0] > self._value:
                return
            for i in range(len(nums_sort)): # O(n^2)
                left = i+1
                right = len(nums_sort) - 1
                while left < right: # O(n)
                    if nums_sort[left] == nums_sort[left+1]:
                        left += 1
                    if nums_sort[right] == nums_sort[right-1]:
                        right -= 1
                    if nums_sort[i] + nums_sort[left] + nums_sort[right] == self._value:
                        self._result.add((nums_sort[i], nums_sort[left], nums_sort[right]))
                        left -= 1
                        right -= 1
                    elif nums_sort[i] + nums_sort[left] + nums_sort[right] < self._value:
                        left += 1
                    elif nums_sort[i] + nums_sort[left] + nums_sort[right] > self._value:
                        right -= 1


    def __enter__(self):
        # self.two_finding()
        # self.three_finding()
        self.three_finding_double_point()
        return self._result
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    # with ThreeSum(nums=[1, 2, 3, 4, 5, 6], value=6) as t1:
    #     print(t1)
    with ThreeSum(nums=[4, -1, 0, 1, 2, -1, -4, -2, 1], value=0) as t2:
        print(t2)
    with ThreeSum(nums=[0, 0, 0], value=0) as t3:
        print(t3)