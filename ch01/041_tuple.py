#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/31
# @Author: Lingchen
# @Prescription: 元组.
#                元组的核心特点是: 不可变序列.
#                元组的访问和处理速度比列表快.
#                与整数和字符串一样,元组可以作为字典的键,列表则永远不能作为作为字典的键使用.

a = (20, 10, 30, 8, 9)
print(a[1])

# 元组元素不可修改.
# TypeError: 'tuple' object does not support item assignment.
# a[1] = 30

# 元组切片.
print(a[1:3])
print(a[:4])
print(a[:])

# 元组排序.
print(sorted(a))

# 元组求和.
print(sum(a))

# zip对象.
# 将多个列表对应位置的元素组合成为元组,并返回这个zip对象.››
a = [10, 20, 30]
b = [40, 50, 60]
c = [70, 80, 90]
d = zip(a, b, c)
print(d)
print(list(d))
