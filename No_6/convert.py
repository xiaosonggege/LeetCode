#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: convert
@time: 2020/6/5 4:25 下午
'''

class Convert:
    def __init__(self, s:str, numRow:int):
        self._s = s
        self._numRow = numRow
        self._result = ''
    def process(self):
        for i in range(self._numRow):
            self._result += self._s[i]
            if i == 0:
                j = i
                while j + (self._numRow - i - 1) * 2 <= len(self._s) - 1:
                    j += (self._numRow - i - 1) * 2
                    self._result += self._s[j]

            elif i > 0 and i <= self._numRow // 2:
                j = i
                flag = 0 #步伐长为0，步伐短为1
                while (j + (self._numRow - i - 1) * 2 <= len(self._s) - 1 and flag == 0) or \
                        (j + i * 2 <= len(self._s) - 1 and flag == 1):
                    j += (self._numRow - i - 1) * 2 if flag == 0 else i * 2
                    self._result += self._s[j]
                    flag = 1 - flag

            elif i == self._numRow - 1:
                j = i
                while j + (self._numRow - 1) * 2 <= len(self._s) - 1:
                    j += (self._numRow - 1) * 2
                    self._result += self._s[j]

            else:
                j = i
                flag = 1  # 步伐长为0，步伐短为1
                while (j + (self._numRow - i - 1) * 2 <= len(self._s) - 1 and flag == 1) or \
                        (j + i * 2 <= len(self._s) - 1 and flag == 0):
                    j += i * 2 if flag == 0 else (self._numRow - i - 1) * 2
                    self._result += self._s[j]
                    flag = 1 - flag

    def __enter__(self):
        self.process()
        return self._result

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with Convert(s='LEETCODEISHIRING', numRow=3) as c:
        print(c)
    with Convert(s='LEETCODEISHIRING', numRow=4) as c:
        print(c)
    with Convert(s='LEETCODEISHIRING', numRow=5) as c:
        print(c)
    with Convert(s='LEETCODEISHIRING', numRow=6) as c:
        print(c)