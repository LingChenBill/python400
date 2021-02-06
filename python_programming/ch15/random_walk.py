#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/6
# @Author: Lingchen
# @Prescription: 随机漫步.
#                随机漫步就是蚂蚁在晕头转向的情况下,每次都沿随机的方向前行所经过的路径.
#                page_315.
from random import choice


class RandomWalk():
    """ 一个生成随机漫步数据的类. """

    def __init__(self, num_points=5000):
        """ 初始化随机漫步的属性. """

        self.num_points = num_points

        # 所有随机漫步都始于(0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ 计算随机漫步包含的所有点.
             向右走还是向左走? 沿指定的方向走多远?
             向上走还是向下走? 沿指定的方向走多远?
             x_step为正:向右移动; 为负:向左移动; 为零:垂直移动.
             y_step为正:向上移动; 为负:向下移动; 为零:水平移动.
        """

        # 不断漫步,直到列表达到指定的长度.
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离.
            # choice 随机返回一个数.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步.
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y的值.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
