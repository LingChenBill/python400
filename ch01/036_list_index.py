#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/29
# @Author: Lingchen
# @Prescription: 列表元素访问与计数.

# 通过列表的索引来获取元素.
a = [10, 20, 30, 40, 50, 60, 70, 20, 30, 40]
print(a[2])

# IndexError: list index out of range.
# print(a[20])

# 获取列表元素所在列表中的索引.
print(a.index(20))

# 获取元素在列表中出现的次数.
print(a.count(20))

# 获取列表的长度.
print(len(a))

# 成员资格判断.
print(20 in a)

print(100 not in a)



