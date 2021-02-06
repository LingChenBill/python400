#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/6
# @Author: Lingchen
# @Prescription: 掷骰子.
#                page_324.
import pygal

from die import Die

# 创建一个D6.
die = Die()

# 掷几次骰子,并将结果存储在一个列表中.
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# print(results)

# 分析结果.
frequencies = []

# 计算每个点数出现的次数.
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# 对结果进行可视化.
# 创建条形图.
hist = pygal.Bar()

# 标示直方图的字符串.
hist.title = "Results of rolling one D6 1000 times."
# 将掷骰子的可能结果用作x轴的标签.
hist.x_labels = ['1', '2', '3', '4', '5', '6']
# 将每个轴x和y轴添加了标题.
hist.x_title = "Result"
hist.y_title = 'Frequency of Result'

# 将一系列的值添加到图表中.
hist.add('D6', frequencies)
# 将这个图表渲染成一个SVG文件.
hist.render_to_file('die_visual.svg')
