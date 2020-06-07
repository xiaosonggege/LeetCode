#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: myAtoi
@time: 2020/6/6 11:38 下午
'''

class MyAtoi:
    def __init__(self, s:str):
        self._s = s

    def change(self):
        result = 0
        temp = 1
        # can_use = {str(i) for i in range(10)}
        # can_use.update('-+')
        for i in self._s:
            if i == '-':
                temp = -1
            elif i >= '0' and i <='9':
                result = result * 10 + int(i)
            elif i == ' ':
                if result == 0:
                    continue
                else:
                    break
            elif i == '+':
                if result == 0:
                    continue
                else:
                    break
            else:
                break
        result *= temp
        return result

    def __enter__(self):
        return self.change()
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    with MyAtoi('42') as m1:
        print(m1)
    with MyAtoi('   -42') as m2:
        print(m2)
    with MyAtoi('4193 with words') as m3:
        print(m3)
    with MyAtoi('2words and 987') as m4:
        print(m4)