#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/6
# @Author: Lingchen
# @Prescription: 绘制随机漫步图.
#                page_316.
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个RandomWalk实例,并将其包含的点都绘制出来.
rw = RandomWalk()
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, edgecolors='none', s=15)
plt.show()
