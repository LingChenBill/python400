#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/6
# @Author: Lingchen
# @Prescription: 绘制一个简单的拆线图.
#                page_306.
import matplotlib.pyplot as plt

int_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# plt.plot(squares)
# plt.plot(squares, linewidth=5)

# 同时提供输入值和输出值.
plt.plot(int_values, squares, linewidth=5)

# 设置图表标题,并给坐标轴加上标签.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小.
plt.tick_params(axis='both', labelsize=14)

plt.show()
