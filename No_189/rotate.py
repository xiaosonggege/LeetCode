#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: rotate
@time: 2020/5/16 11:54 下午
'''
import copy

class Rotate:
    def __init__(self, nums:list, k:int):
        self._nums = nums
        self._k = k
    def rotate_func1(self, nums:list, k:int)->list:
        nums = copy.deepcopy(nums)
        l = len(nums)
        time = 0
        move = 0
        while time < l-k:
            temp = nums[0]
            while move < l-1:
                nums[move] = nums[move+1]
                move += 1
            nums[l-1] = temp
            time += 1
            move = 0
        return nums

    def rotate_func2(self, nums:list, k:int)->list:
        nums = copy.deepcopy(nums)
        l = len(nums)
        time = 0
        while time < k:
            move = l - 1
            temp = nums[l-1]
            while move > 0:
                nums[move] = nums[move - 1]
                move -= 1
            nums[0] = temp
            time += 1
        return nums

    def rotate_func3(self, nums:list, k:int)->list:
        nums = copy.deepcopy(nums)
        move = 0
        l = len(nums)
        while move < k:
            r = move + l - k
            nums[move], nums[r] = nums[r], nums[move]
            move += 1

        move1 = move
        time = 0
        while time < l-k-move1:
            move = move1
            temp = nums[move1]
            while move < l - 1:
                nums[move] = nums[move + 1]
                move += 1
            nums[move] = temp
            time += 1
        return nums

    def rotate_func4(self, k:int)->None: #环形队列队头队尾指针移动o(n),o(1)
        l = self._nums.__len__()
        if not hasattr(self, '_start'):
            self._start = 0
        if not hasattr(self, '_end'):
            self._end = l - 1
        self._start += l - k
        self._end  = (self._end + l - k) % l

    def rotate_func4_read_func(self)->list:
        l = self._nums.__len__()
        nums = []
        start = self._start
        while start != self._end:
            nums.append(self._nums[start])
            start = (start + 1) % l
        nums.append(self._nums[start])
        return nums

    def __enter__(self):
        self.rotate_func4(k=5)
        return self.rotate_func4_read_func()
        # return self.rotate_func1(self._nums, self._k), self.rotate_func2(self._nums, self._k), \
        #        self.rotate_func3(self._nums, self._k)
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with Rotate(nums=[1,2,3,4,5,6,7,8,9], k=3) as r:
        print(r)