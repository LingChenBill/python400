#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/31
# @Author: Lingchen
# @Prescription: 字典元素的访问.
#                通过键来获取值.

# 通过键来获取值.
a = {'name': 'John', 'age': 18, 'job': 'programmer'}
print(a['name'])

# KeyError: 'sex'.
# print(a['sex'])

# 通过get()方法来获取值.
print(a.get('name'))
# None.
print(a.get('sex'))
print(a.get('sex', "不存在"))

# 列出所有键值对.
print(a.items())

# 列出所有的键,列出所有的值.
print(a.keys())
print(a.values())

# 键值结的个数.
print(len(a))

# 检测一个键是否在字典中.
print('name' in a)
