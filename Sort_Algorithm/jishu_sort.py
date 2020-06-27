#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: radix_sort
@time: 2020/6/27 1:32 下午
'''

class Jishusort:
    def __init__(self, nums:list, k:int=10):
        self._nums = nums
        self._k = k

    def process(self)->list: #时间复杂度为O(n+k),空间复杂度为O(n+k)
        #建立临时存储块
        nums1 = [0] * self._k
        #将待排序数组中的数作为nums1数组的索引，存入待排序数组元素个数
        for i in self._nums: # O(n)
            nums1[i] += 1
        count = nums1[0]
        flag = 0
        for i in range(1, len(nums1)): # O(n)
            count += nums1[i]
            if count == len(self._nums):
                flag = 1
            nums1[i] += nums1[i-1]
            if flag == 1:
                break
        #建立最终的排序数组
        nums2 = [0] * len(self._nums)
        #最后一步必须采用倒序，因为要保证基数排序的稳定性，如果正序，则相同值会颠倒顺序!
        for i in reversed(self._nums): # O(n)
            nums2[nums1[i]-1] = i
            nums1[i] -= 1
        return nums2

    def __enter__(self):
        nums2 = self.process()
        return nums2
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with Jishusort(nums=[2, 5, 3, 0, 2, 3, 0, 3]) as j1:
        print(j1)
    with Jishusort(nums=list(range(8, 0, -1))) as j2:
        print(j2)