#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: majorityElement
@time: 2020/5/9 9:29 上午
'''
import copy
class MajorityElement:
    def __init__(self, nums:list):
        self._nums = nums
        self._target = None

    def insert_sort(self)->list:
        nums = copy.deepcopy(self._nums)
        flag = nums[0]
        for i in range(1, len(self._nums)):
            flag = nums[i]
            for j in range(i-1, -1, -1):
                if nums[j] > flag:
                    nums[j+1] = nums[j]
                else:
                    nums[j+1] = flag
                    break
                if j == 0:
                    nums[0] = flag
        return nums

    def merger_sort_sub(self, nums1:list, nums2:list)->list:
        result = []
        while len(nums1) and len(nums2):
            result.append(nums1.pop(0) if nums1[0] <= nums2[0] else nums2.pop(0))
        result.extend(nums1 if len(nums1) else nums2)
        return result

    def merger_sort(self, nums:list)->list:
        if len(nums) > 1:
            nums_l, nums_r = nums[:len(nums)//2+1], nums[len(nums)//2+1:]
            self.merger_sort(nums_l)
            self.merger_sort(nums_r)
        nums = self.merger_sort_sub(nums1=nums_l, nums2=nums_r)

    def mE(self):
        return self.insert_sort()[self.insert_sort().__len__()//2]


if __name__ == '__main__':
    m = MajorityElement(nums=[2, 1, 5, 3, 6, 4, 7, 2, 2, 2, 2, 2])
    # print(m.insert_sort())
    # print(m.mE())
    print(m.merger_sort_sub(nums1=[1, 2, 3, 5], nums2=[2, 4, 6, 7]))