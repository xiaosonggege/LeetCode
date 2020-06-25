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
    def __init__(self, nums:list, queue:list):
        '''
        @param nums: 任务等级序列
        @param queue: 任务序列
        '''
        super().__init__(nums=nums)
        self._dict = {i:j for i, j in zip(self._nums, queue)}

    def insert(self, *group):
        '''
        入队
        '''
        self.build_max_heap() # O(nlogn)
        num, task = group
        self._dict[num] = task
        self._nums.append(num)
        self._length_size += 1
        i = self._length_size
        while self._nums[self._parient(i)-1] < self._nums[i-1] and i-1 > 0: # O(logn)
            self._nums[self._parient(i)-1], self._nums[i-1] = self._nums[i-1], self._nums[self._parient(i)-1]
            i = self._parient(i)
        return

    def maximum(self): # O(nlogn)
        '''
        返回队列中最大元素
        '''
        #构建最大堆
        self.build_max_heap() # O(nlogn)
        #返回堆顶元素
        return self._dict[self._nums[0]]

    def extract_max(self): # O(nlogn)
        '''
        提取队列中最大元素
        '''
        #构建最大堆
        self.build_max_heap() # O(nlogn)
        #将最优任务从堆中去除
        self._nums[0], self._nums[self._length_size-1] = self._nums[self._length_size-1], self._nums[0]
        max = self._nums[self._length_size - 1]
        self._length_size -= 1
        self.max_heapify(1) # O(logn)
        return self._dict[max]

    def increase_key(self, x, k): # O(nlogn)
        '''
        将队列中元素关键字增加到k
        '''
        self.build_max_heap() # O(nlogn)
        indice = self._nums.index(x) # O(logn)
        self._nums[indice] = k
        task = self._dict.pop(x)
        self._dict[k] = task
        i = indice + 1
        while self._nums[self._parient(i) - 1] < self._nums[i - 1] and i - 1 > 0:  # O(logn)
            self._nums[self._parient(i) - 1], self._nums[i - 1] = self._nums[i - 1], self._nums[self._parient(i) - 1]
            i = self._parient(i)
        return


    def __enter__(self):
        # return self.maximum()
        # return self.extract_max()
        # self.insert(6, 'f')
        self.increase_key(4, 5)

if __name__ == '__main__':
    # with Heap(nums=[1, 2, 3, 4, 5]) as h1:
    #     pass
    with PriorityQueue(nums=[1, 2, 3, 4, 5], queue=['a', 'b', 'c', 'd', 'e']) as P1:
        print(P1)