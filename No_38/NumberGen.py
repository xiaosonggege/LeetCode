#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: NumberGen
@time: 2020/2/16 22:24 下午
'''
class CountAndSay:
    def __init__(self, num):
        """
        构造函数
        :param num: 输出到的位置项
        """
        self._num = num
        self._num_n = num
        self._str = '1'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True

    def __iter__(self):
        return self

    def __next__(self):
        if self._num == self._num_n:
            self._num -= 1
            return self._str
        elif self._num:
            pos = 0
            count = 0
            str_temp = []
            while pos != len(self._str):
                if len(self._str) == 1:
                    str_temp = [str(1), self._str]
                else:
                    if not pos: #是第一个位置
                        count += 1
                    elif pos != len(self._str) - 1: #不是最后一个位置
                        if self._str[pos] != self._str[pos-1]:
                            str_temp.append(str(count))
                            count = 1
                            str_temp.append(self._str[pos-1])
                        else:
                            count += 1
                    else: #是最后一个位置
                        if self._str[pos] != self._str[pos-1]:
                            str_temp.append(str(count))
                            count = 1
                            str_temp.append(self._str[pos-1])
                            str_temp.append(str(count))
                            str_temp.append(self._str[pos])
                        else:
                            str_temp.append(str(count + 1))
                            str_temp.append(self._str[pos])

                pos += 1
            self._num -= 1
            self._str = ''.join([str(e) for e in str_temp])
            return self._str
        else:
            raise StopIteration


if __name__ == '__main__':
    with CountAndSay(7) as c:
        for i in c:
            print(i)
