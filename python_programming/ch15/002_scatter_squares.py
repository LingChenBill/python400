#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/6
# @Author: Lingchen
# @Prescription: 绘制散点图,并设置其样式.
#                matplotlib允许你给散点图中的各个点指定颜色,默认为蓝色点和黑色轮廓.
#                page_309.
import matplotlib.pyplot as plt

# plt.scatter(2, 4)
# plt.scatter(2, 4, s=200)

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=100)

# 自动计算数据.
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values, s=40)

# 删除数据点的黑色轮廓.
# plt.scatter(x_values, y_values, edgecolors='none', s=40)

# 自定义数据点的颜色.
# plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)

# 使用RGB颜色.值越接近0,指定的颜色越深,值越接近1,指定的颜色越浅.
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=40)

# 使用颜色映射.
# 颜色映射,是一系列颜色,从起始颜色渐变到结束颜色.
# 在可视化中,颜色映射可用于突出数据的规律.
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# 设置图表标题并给坐标轴加上标签.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小.
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围.x和y值的最小值与最大值.
plt.axis([0, 1100, 0, 1100000])

# plt.show()

# 自动保存图表.与plt.show()互斥.
# bbox_inches将图表多余的空白区域裁剪掉.保留则不设置.
# plt.savefig('002_squares_plot.png')
plt.savefig('002_squares_plot.png', bbox_inches='tight')
