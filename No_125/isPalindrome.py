#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: isPalindrome
@time: 2020/5/4 3:15 下午
'''


class IsPalinDrome:

    @staticmethod
    def range_judge(e:str):
        if e.lower() >= 'a' and e.lower() <= 'z' or e >= '0' and e <= '9':
            return True
        else:
            return False

    def __init__(self, strs:str):
        self._strs = strs

    def judge(self, i:int, j:int):
        # print(self._strs[i], self._strs[j])
        #j索引位置不是可判断字符
        if not IsPalinDrome.range_judge(self._strs[j]):
            if j > i+1:
                self.judge(i, j-1)
            else:
                print('True')
        #i索引位置不是可判断字符
        if not IsPalinDrome.range_judge(self._strs[i]):
            if i < j-1:
                self.judge(i+1, j)
            else:
                print('True')
        #i和j位置的字符都是可以判断字符时
        if IsPalinDrome.range_judge(self._strs[i]) and IsPalinDrome.range_judge(self._strs[j]):
            if self._strs[i].lower() != self._strs[j].lower():
                print('False')
            elif j - i >= 3:  # 中间间隔两个
                self.judge(i+1, j-1)
            else:
                print('True')

    def __enter__(self):
        self.judge(0, self._strs.__len__()-1)
        return None
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':
    with IsPalinDrome('A man, a plan, a canal: Panama') as m:
        pass
    with IsPalinDrome('race a car') as n:
        pass