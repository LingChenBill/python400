#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/6
# @Author: Lingchen
# @Prescription: 模拟掷一个骰子的类.
#                page_323.
from random import randint


class Die():
    """ 表示一个骰子的类. """

    def __init__(self, num_sides=6):
        """ 骰子默认为6. """

        self.num_sides = num_sides

    def roll(self):
        """ 返回一个位于1和骰子页数之间的随机数. """

        return randint(1, self.num_sides)

