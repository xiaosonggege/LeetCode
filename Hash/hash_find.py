#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: hash_find
@time: 2020/5/13 6:12 下午
'''

class HashTable1:
    """
    线性探测法的hash查找
    """
    def __init__(self, size:int):
        self._size = size
        self._keys = [None] * size #键
        self._values = [None] * size #值

    #hash函数可通过猴子补丁类外自行设计
    def hashfunction(self, key, size)->int:
        """
        哈希函数
        """
        return key % size

    #冲突函数可通过猴子补丁类外自行设计
    def rehash(self, oldhash, size)->int:
        """
        冲突解决函数
        """
        return (oldhash + 1) % size

    def _put(self, key, value)->None:
        """
        哈希表建立
        """
        #获得哈希函数值
        hashvalue = self.hashfunction(key=key, size=self._size)
        if self._keys[hashvalue] is None: #位置为空
            self._keys[hashvalue] = key
            self._values[hashvalue] = value
        else: #位置非空
            if self._keys[hashvalue] == key: #位置上key已存在
                self._values[hashvalue] = value
            else: #发生冲突
                #解决冲突
                new_hashvalue = self.rehash(oldhash=hashvalue, size=self._size)
                while self._keys[new_hashvalue] is not None and self._keys[new_hashvalue] != key \
                        and new_hashvalue != hashvalue:
                    new_hashvalue = self.rehash(oldhash=new_hashvalue, size=self._size)
                if self._keys[new_hashvalue] is None:
                    self._keys[new_hashvalue] = key
                if new_hashvalue != hashvalue:
                    self._values[new_hashvalue] = value
                else:
                    print('hash表已满,无法插入!')

    def _get(self, key):
        """
        哈希表查找
        """
        # 获得哈希函数值
        hashvalue = self.hashfunction(key=key, size=self._size)
        # find = False
        value = None
        if self._keys[hashvalue] == key:
            value = self._values[hashvalue]
        else:
            #重新哈希
            new_hashvalue = self.rehash(oldhash=hashvalue, size=self._size)
            while self._keys[new_hashvalue] is not None and self._keys[new_hashvalue] != key \
                    and hashvalue != new_hashvalue:
                new_hashvalue = self.rehash(oldhash=new_hashvalue, size=self._size)
            if self._keys[new_hashvalue] == key:
                value = self._values[new_hashvalue]
        return value

    def __getitem__(self, item):
        return self._get(key=item)

    def __setitem__(self, key, value):
        return self._put(key=key, value=value)

class HashTable2:
    """
    拉链法的hash查找
    """
    pass

if __name__ == '__main__':
    H = HashTable1(size=11)
    H[54] = "cat" #余10
    H[26] = "dog" #余4
    H[93] = "lion" #余5
    H[17] = "tiger" #余6
    H[77] = "bird" #余0
    H[31] = "cow" #余9
    H[44] = "goat" #余0
    H[55] = "pig" #余0
    H[20] = "chicken" #余9

    print(H._keys)  # [77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]
    print(H._values)  # ['bird', 'goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']
    print(H[20])  # chicken
    H[20] = 'duck'
    print(H[20])  # duck
    print(H[99])  # None
    print(H[45]) # None
    print(H[44]) # goat