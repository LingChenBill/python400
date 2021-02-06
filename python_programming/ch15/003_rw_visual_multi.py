#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/6
# @Author: Lingchen
# @Prescription: 绘制随机漫步图.
#                page_316.
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态,就不断地模拟随机漫步.
while True:

    # 创建一个RandomWalk实例,并将其包含的点都绘制出来.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 使用颜色映射来指出漫步中各点的先后顺序,并删除每个点的黑色轮廓,让它们的颜色更明显.
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    # plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # 模拟花粉在水滴表面的运动路径.
    # plt.plot(rw.x_values, rw.y_values, c='blue', linewidth=5)

    # 突出起点与终点.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # 设置绘制窗口的尺寸.
    # Python假定屏幕分辨率为80像素/英寸.
    # plt.figure(figsize=(10, 6))
    plt.figure(dpi=128, figsize=(10, 6))

    plt.show()

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break

