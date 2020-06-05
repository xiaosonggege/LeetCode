#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: longestPalindrome
@time: 2020/6/1 4:06 下午
'''

class LongestPalindrome:
    def __init__(self, s:str):
        self._s = s
        self._max = 1 #最长回文字符串长度
        self._result_left = 0 #结果左边界
        self._result_right = 0 #结果右边界
        #DP算法存储存储空间
        self._dp_matrix = [[False for _ in range(len(self._s))] for _ in range(len(self._s))]

    def _process(self):
        for l in range(1, len(self._s)+1):
            for i in range(len(self._s)-l+1):
                if self._s[i] == self._s[i+l-1]:
                    if l <= 2 or self._dp_matrix[i+1][i+l-2]:
                        self._dp_matrix[i][i+l-1] = True
                        self._max = max(self._max, l)
                        self._result_left, self._result_right = i, i+l-1

    def __enter__(self):
        self._process()
        return self._max, self._s[self._result_left:self._result_right+1]

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with LongestPalindrome(s='babad') as l1:
        print(l1[0], l1[1])
    with LongestPalindrome(s='cbbd') as l2:
        print(l2[0], l2[1])
    with LongestPalindrome(s='babaddabab') as l3:
        print(l3[0], l3[1])
