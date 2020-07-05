#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: kd_tree
@time: 2020/7/2 2:02 下午
'''
import numpy as np
import _bisect

class TreeProperty:
    def __init__(self, name:str):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value

class Tree:
    def __init__(self, value=None, lchild=None, rchild=None):
        self._value = value
        self._lchild = lchild
        self._rchild = rchild

    def __eq__(self, other):
        return True
    def __le__(self, other):
        return True
    def __lt__(self, other):
        return True
    def __ge__(self, other):
        return True
    def __gt__(self, other):
        return True

    value = TreeProperty('_value')
    lchild = TreeProperty('_lchild')
    rchild = TreeProperty('_rchild')

class KdTree:
    def __init__(self, dataset:np.ndarray, k:int, num_in_leaf:int, num_nearest:int, max_trackback:int):
        '''
        :param dataset: 二维矩阵，第一个维度是数据量，第二个维度是特征数
        :param k: 需要找出k个最近邻
        :param num_in_leaf: 叶子节点中数据数量最大值
        :param num_nearest: 最近邻数量
        :param max_trackback: 最大回溯次数
        '''
        self._dataset = dataset
        self._k = k
        self._num_in_leaf = num_in_leaf
        self._root = Tree(value=None) #初始化kd-tree根节点
        self._num_of_traceback = 0 #回溯次数
        self._num_nearest = num_nearest #最近邻数量
        self._max_trackback = max_trackback #最大回溯次数
        self._knn_result = None #最近邻查找结果

    def _build(self, dataset:np.ndarray, root:Tree): # O(n)时间复杂度，O(n)空间复杂度
        '''
        建立kd-tree
        '''
        #求出最大方差所在维度 # O(n^2)
        max_var_dim = np.argmax(np.var(dataset, axis=0))
        #求出该维度特征中位数 O(n)
        dim_median = np.median(dataset[:, max_var_dim])
        # O(n)
        left_dataset = dataset[dataset[:, max_var_dim]<=dim_median, :]
        right_dataset = dataset[dataset[:, max_var_dim]>dim_median, :]
        root.value = (max_var_dim, dim_median)
        root.lchild = Tree()
        root.rchild = Tree()
        if left_dataset.shape[0] > self._num_in_leaf:
            self._build(dataset=left_dataset, root=root.lchild)
        else:
            root.lchild.value = left_dataset

        if right_dataset.shape[0] > self._num_in_leaf:
            self._build(dataset=right_dataset, root=root.rchild)
        else:
            root.rchild.value = right_dataset

    def __call__(self, data:np.ndarray):
        self._build(dataset=self._dataset, root=self._root)
        print('建树完毕')
        self.knn_finding(data=data, root=self._root, queue=[])
        return self._knn_result

    def knn_finding(self, data:np.ndarray, root:Tree, queue:list): #O(nlogn)时间复杂度 O(n)空间复杂度
        '''
        搜索k个近邻
        :param data: 目标数据
        :param queue: 访问队列，按照目标数据与双亲节点对应维度距离从小到大存储
        '''
        if root.value.__class__ == tuple: #非叶子结点
            dim = root.value[0]
            diff = data[dim] - root.value[-1]
            #root插入queue的位置
            #################
            if diff > 0:
                if root.rchild is not None:
                    if root.lchild is not None: # O(logn)
                        _bisect.insort_right(queue, (abs(diff), root.lchild))
                    self.knn_finding(data=data, root=root.rchild, queue=queue)
            else:
                if root.lchild is not None:
                    if root.rchild is not None:
                        _bisect.insort_right(queue, (abs(diff), root.rchild))
                    self.knn_finding(data=data, root=root.lchild, queue=queue)
        else: #叶子结点
            #找到num_nearest个近邻，宁少勿缺
            self._knn_result = root.value if self._knn_result is None else \
                np.vstack((self._knn_result, root.value))
            #先排序后截取前num_nearest个 # O(nlogn)
            dis = np.sum((self._knn_result - data) ** 2, axis=1)
            self._knn_result = self._knn_result[np.argsort(dis)][:self._num_nearest, :]
            #回溯
            if self._num_of_traceback < self._max_trackback:
                self._num_of_traceback += 1
                root_new = queue.pop(0)[-1]
                self.knn_finding(data=data, root=root_new, queue=queue)


if __name__ == '__main__':
    dataset = np.array([
        [2, 3],
        [5, 4],
        [9, 6],
        [4, 7],
        [8, 1],
        [7, 2]
    ])
    kdtree = KdTree(dataset=dataset, k=1, num_in_leaf=2, num_nearest=7, max_trackback=3)
    knn = kdtree(data=np.array([5.5, 5]))
    print(knn)
