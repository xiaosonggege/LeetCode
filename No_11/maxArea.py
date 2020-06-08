#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: No_11
@time: 2020/6/7 11:36 上午
'''

class MaxArea:
    def __init__(self, heights:list):
        self._heights = heights
        self._left_edge = 0
        self._right_edge = len(self._heights) - 1
        self._max_area = 0

    def process(self, left, right, min_short, flag=0):
        if left != right:
            if flag == 0:  # 上次最小值出现在左指针位置
                if self._heights[left] <= min_short:  # 如果左指针向右移动后的索引位置依然比原左指针索引位置小，继续向右
                    self.process(left=left + 1, right=right, min_short=min_short, flag=0)
                else:
                    min_short = min(self._heights[left], self._heights[right])
                    s = (right - left) * min_short
                    if s > self._max_area:
                        self._max_area = s
                        self._left_edge, self._right_edge = left, right
                    if self._heights[left] == min_short:
                        self.process(left=left + 1, right=right, min_short=min_short, flag=0)
                    elif self._heights[right] == min_short:
                        self.process(left=left, right=right - 1, min_short=min_short, flag=1)
            elif flag == 1:  # 上次最小值出现在右指针位置
                if self._heights[right] <= min_short:  # 如果右指针向左移动后的索引位置依然比原右指针索引位置小，继续向左
                    self.process(left=left, right=right - 1, min_short=min_short, flag=1)
                else:
                    min_short = min(self._heights[left], self._heights[right])
                    s = (right - left) * min_short
                    if s > self._max_area:
                        self._max_area = s
                        self._left_edge, self._right_edge = left, right
                    if self._heights[left] == min_short:
                        self.process(left=left + 1, right=right, min_short=min_short, flag=0)
                    elif self._heights[right] == min_short:
                        self.process(left=left, right=right - 1, min_short=min_short, flag=1)

    def __enter__(self):
        min_short = min(self._heights[self._left_edge], self._heights[self._right_edge])
        flag = 0 if self._heights[self._left_edge] == min_short else 1
        self.process(left=self._left_edge, right=self._right_edge, min_short=min_short, flag=flag)
        return self._max_area, self._left_edge, self._right_edge

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with MaxArea(heights=[1,8,6,2,5,4,8,3,7]) as m:
        print(m)
    with MaxArea(heights=[1, 4, 3, 2, 5, 7, 34, 99, 9]) as m2:
        print(m2)