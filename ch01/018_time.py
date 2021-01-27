#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/27
# @Author: Lingchen
# @Prescription: 时间的表示.
#                计算机中时间的表示是从1970/1/1 00:00:00开始,以毫秒进行计算.这个时刻也叫做unix时间点.
import time

# 获取当前时间.
a = time.time()
print(a)

# 获取当前秒数.
b = int(a)
print(b)

# 分钟数.
minutes = b / 60
print(minutes)
minutes = b // 60
print(minutes)

# 小时数.
hours = minutes // 60
print(hours)

# 天数.
days = hours // 24
print(days)

# 年数.
years = days // 365
print(years)

