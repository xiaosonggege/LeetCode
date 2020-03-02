#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: addBinary
@time: 2020/2/18 3:18 下午
'''
class AddBinary:
    def __init__(self, val:str)->None:
        self._val = val

    @property
    def val(self):
        return self._val

    def _binary_add(self, *para)->tuple:
        jinwei = '0'
        lis = [int(i) for i in para]
        if sum(lis) == 2:
            jinwei = '1'
            result = '0'
        elif sum(lis) == 3:
            jinwei = '1'
            result = '1'
        else:
            result = str(sum(lis))
        return result, jinwei

    def _add(self, *xy):
        x, y = sorted(xy, key=len)
        x = '0' * (len(y) - len(x)) + x
        result_list = []
        jinwei = '0'
        range_inf = -len(x) - 1
        for index in range(-1, range_inf, -1):
            result_per, jinwei_per = self._binary_add(x[index], y[index], jinwei)
            if not int(jinwei_per):  # 无需进位
                result_list.insert(0, result_per)
            else:
                result_list.insert(0, result_per)
            jinwei = jinwei_per
        if jinwei == '1':
            return jinwei + ''.join(result_list)
        return ''.join(result_list)

    def __add__(self, other):
        if isinstance(other, AddBinary):
            x, y = self.val, other.val
            return self._add(x, y)
        elif isinstance(other, str):
            return self._add(self._val, other)
        else:
            raise TypeError('类型错误!')

if __name__ == '__main__':
    a = AddBinary('11')
    b = AddBinary('1')
    c = '1010'
    d = AddBinary('1011')
    try:
        print(a + b)
        print(d + c)
    except TypeError as e:
        print(e)
    finally:
        print('over')
