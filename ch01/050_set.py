#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/31
# @Author: Lingchen
# @Prescription: 集合.
#                集合是无序可变的,元素不可重复.

# 集合创建.
a = {3, 5, 7}
print(a)
print(type(a))

# 集合添加元素.
a.add(9)
print(a)

b = ['a', 'b', 'c', 'd']
c = set(b)
print(c)

# 集合元素删除.
c.remove('b')
print(c)

a = {1, 3, 'python'}
b = {1, 'it', 'hello'}

# 并集.
print(a | b)

# 交集.
print(a & b)
print(a.intersection(b))

# 差集.
print(a - b)
print(a.difference(b))

# 并集.
print(a.union(b))
