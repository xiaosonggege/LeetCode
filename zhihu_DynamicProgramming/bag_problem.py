#!/usr/bin/env python
# encoding: utf-8
'''
@author: songyunlong
@license: (C) Copyright 2020-2025.
@contact: 1243049371@qq.com
@software: pycharm
@file: bag_problem
@time: 2020/5/25 4:42 下午
'''
import copy
class BagProblem:
    def __init__(self, cost:list, value:list, cost_max:int):
        self._cost = cost #代价数组
        # 对代价数组中元素数量上的限制，0/1背包问题用
        self._cost_number_limit = [1] * self._cost.__len__()
        self._value = value #价值数组
        self._cost_max = cost_max #代价上界
        self._value_max = 0 #最终所获价值

    def total_problem(self, cost_max:int):
        """
        完全背包问题
        :param cost_max: 当前代价上界
        """
        value_max = 0
        for i in range(self._cost.__len__()):
            if cost_max - self._cost[i] >= 0:
                value_max = max(value_max, self._value[i] + self.total_problem(cost_max=cost_max - self._cost[i]))
            else:
                continue
        return value_max

    def zero_or_one(self, cost_max:int):
        """
        0/1背包问题
        :param cost_max: 当前代价上界
        """
        value_max = 0
        for i in range(self._cost.__len__()):
            if cost_max - self._cost[i] >= 0 and self._cost_number_limit[i]:
                self._cost_number_limit[i] -= 1
                value_max = max(value_max, self._value[i] + self.zero_or_one(cost_max=cost_max - self._cost[i]))
            else:
                continue
        return value_max

if __name__ == '__main__':
    b1 = BagProblem(cost=[71, 69, 1], value=[100, 1, 2], cost_max=70)
    # print(b1.total_problem(b1._cost_max))
    print(b1.zero_or_one(b1._cost_max))