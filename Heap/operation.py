#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: operation
@time: 2020/6/24 3:21 下午
'''
import math
class Heap:

    def __init__(self, nums:list):
        self._nums = nums
        self._length = 100 #记录堆的可存储容量
        self._length_size = len(self._nums) #记录堆的实际长度
        self._parient = lambda i: i // 2
        self._leftchild = lambda i: 2 * i
        self._rightchild = lambda i: 2 * i + 1

    def max_heapify(self, i:int): # 时间复杂度O(logn)，空间复杂度O(1)
        '''
        维护堆结构
        '''
        temp = i
        if self._leftchild(i) <= self._length_size and self._nums[i-1] < self._nums[self._leftchild(i)-1]:
            i = self._leftchild(i)
        if self._rightchild(temp) <= self._length_size and self._nums[i-1] < self._nums[self._rightchild(temp)-1]:
            i = self._rightchild(temp)
        if i != temp:
            self._nums[i-1], self._nums[temp-1] = self._nums[temp-1], self._nums[i-1]
            self.max_heapify(i=i)

    def build_max_heap(self): # 时间复杂度O(nlogn), 空间复杂度O(1)
        '''
        建立最大(最小堆)
        '''
        for i in range(int(math.log2(self._length_size)), 0, -1):
            self.max_heapify(i=i)

    def heapsort(self): #时间复杂度O(nlogn), 空间复杂度O(1)
        '''
        堆排序
        '''
        #先建立最大堆
        self.build_max_heap() #O(nlogn)
        while self._length_size: #O(nlogn)
            self._nums[0], self._nums[self._length_size-1] = self._nums[self._length_size-1], self._nums[0]
            self._length_size -= 1
            self.max_heapify(i=1)

    def __enter__(self):
        self.heapsort()
        return
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class PriorityQueue(Heap):
    def __init__(self, nums:list):
        super().__init__(nums=nums)
        pass
    def insert(self, x):
        '''
        入队
        '''
        pass

    def maximum(self):
        '''
        返回队列中最大元素
        '''
        pass

    def extract_max(self):
        '''
        提取队列中最大元素
        '''
        pass

    def increase_key(self, x, k):
        '''
        将队列中元素关键字增加到k
        '''
        pass


if __name__ == '__main__':
    with Heap(nums=[1, 2, 3, 4, 5]) as h1:
        pass