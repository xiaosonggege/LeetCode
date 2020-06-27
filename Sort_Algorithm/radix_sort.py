#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: Radix_sort
@time: 2020/6/27 2:34 下午
'''
from Sort_Algorithm.jishu_sort import Jishusort

class Radixsort:
    def __init__(self, nums:list, k:int=20):
        self._nums = nums
        self._k = k

    def process(self)->list:
        #按位截取
        wei = 0
        while True: # O(位数*n)
            #存储指定位的值
            nums_wei = []
            for i in self._nums: # O(n)
                nums_wei.append((i//(10**wei))%10)
            if max(nums_wei) == 0:
                break
            # 建立临时存储块
            nums1 = [0] * self._k
            # 将待排序数组中的数作为nums1数组的索引，存入待排序数组元素个数
            for i in range(len(nums_wei)):  # O(n)
                nums1[nums_wei[i]] += 1
            for i in range(1, len(nums1)):  # O(n)
                nums1[i] += nums1[i - 1]
            # 建立最终的排序数组
            nums2 = [0] * len(self._nums)
            # 最后一步必须采用倒序，因为要保证基数排序的稳定性，如果正序，则相同值会颠倒顺序!
            for i in range(len(nums_wei)-1, -1, -1): #reversed(self._nums):  # O(n)
                nums2[nums1[nums_wei[i]] - 1] = self._nums[i]
                nums1[nums_wei[i]] -= 1
            wei += 1
            self._nums = nums2

        return self._nums

    def __enter__(self):
        nums = self.process()
        return nums
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with Radixsort(nums=[329, 457, 657, 839, 436, 720, 355]) as r1:
        print(r1)
    with Radixsort(nums=[99, 2, 84, 100, 1]) as r2:
        print(r2)