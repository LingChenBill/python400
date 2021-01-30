#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/30
# @Author: Lingchen
# @Prescription: 导入整个模块.
# noinspection PyUnresolvedReferences
# import pizza

# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# from pizza import make_pizza
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 给函数make_pizza指定别名 mp.
# from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用 as 给模块指定别名.
# import pizza as p
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用星号(*) 运算符可让python导入模块中的所有函数.
# Python可以遇到多个名称相同的函数或者变量,进而覆盖函数,而不是分别导入所有的函数.
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
