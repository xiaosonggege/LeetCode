#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: intToRoman
@time: 2020/6/7 3:10 下午
'''

class IntToRoman:
    table = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC',
             100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
    lis = list(table.keys())
    def __init__(self, num:int):
        self._num = num
        self._roman = ''

    def find2f(self, left, right):
        mid = (left + right) // 2
        # if self._num == IntToRoman.lis[mid]:
        #     self._roman += IntToRoman.table[self._num]
        if self._num >= IntToRoman.lis[mid]:
            if mid < len(IntToRoman.lis) - 1:
                if self._num < IntToRoman.lis[mid+1]:
                    n = self._num // IntToRoman.lis[mid]
                    self._roman += IntToRoman.table[IntToRoman.lis[mid]] * n
                    self._num -= IntToRoman.lis[mid] * n
                    if self._num != 0: #不用检查mid-1和left的关系，若num=0，其中包括了mid=0的情况
                        self.find2f(left=0, right=mid - 1) # 已经确定新的待计算值比mid索引位置的值小
                elif self._num != 0:
                    self.find2f(left=mid+1, right=right)

            else: # mid索引为最后一个值
                n = self._num // IntToRoman.lis[mid]
                self._roman += IntToRoman.table[IntToRoman.lis[mid]] * n
                self._num -= IntToRoman.lis[mid] * n
                if self._num != 0:
                    self.find2f(left=0, right=mid - 1)  # 已经确定新的待计算值比mid索引位置的值小

        elif self._num < IntToRoman.lis[mid]: #待计算值比mid索引位置的值小
            if self._num != 0:
                self.find2f(left=left, right=mid-1)

    def __enter__(self):
        self.find2f(left=0, right=len(IntToRoman.lis)-1)
        return self._roman

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with IntToRoman(num=12) as i1:
        print(i1)
    with IntToRoman(num=1222) as i2:
        print(i2)
    with IntToRoman(num=4) as i3:
        print(i3)
    with IntToRoman(num=9) as i4:
        print(i4)
    with IntToRoman(num=58) as i5:
        print(i5)
    with IntToRoman(num=1994) as i6:
        print(i6)
    with IntToRoman(num=1000) as i7:
        print(i7)