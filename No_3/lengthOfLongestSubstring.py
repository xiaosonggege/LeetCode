#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: lengthOfLongestSubstring
@time: 2020/5/27 4:21 下午
'''

class LengthOfLongestSubstring:
    def __init__(self, s:str):
        self._s = s
        self._max_length = 0
    def finding(self):
        start = 0
        end = 0
        move = 0
        while move != len(self._s)-1:
            move += 1
            try:
                pos = self._s.index(self._s[move], start, end+1) #o(logn)复杂度
            except ValueError:
                pos = None
            if pos is not None: #move处的值和前边start与end+1之间的值有重复
                self._max_length = max(self._max_length, end-start+1)
                start = pos + 1
            end = move
        return self._max_length

if __name__ == '__main__':
    l = LengthOfLongestSubstring(s='abcabcbb')
    print(l.finding())
    l1 = LengthOfLongestSubstring(s='bbbbb')
    print(l1.finding())
    l2 = LengthOfLongestSubstring(s='pwwkew')
    print(l2.finding())