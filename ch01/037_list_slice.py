#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/29
# @Author: Lingchen
# @Prescription: 列表的切片.
#                列表的遍历.

# 提取整个列表.
a = [10, 20, 30, 40, 50]
print(a[:])

# [start: end: step],前闭后合
print(a[1:])

print(a[:2])

print(a[1:3])

print(a[1:5:2])

# 逆序,也是前闭后合.
print(a[-3:])

print(a[-5:-3])

print(a[::-1])

# 列表的遍历.
for b in a:
    print(b)

