#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: __init__.py
@time: 2020/2/18 3:18 下午
'''
import re

if __name__ == '__main__':
    s = 'Hello Bingqian! My name is Shagua!'
    regex = re.compile(pattern='[A-Za-z]+', flags=re.IGNORECASE)
    result = regex.finditer(string=s)
    res = [i.group(0) for i in result]
    print(res[-1], len(res[-1]))