#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/31
# @Author: Lingchen
# @Prescription: 生成器推导式创建元组.
#                生成器推导式生成的不是列表也不是元组,而是一个生成器对象.
#                通过生成器对象,转化成列表或者元组.

# 生成器对象.
s = (x * 2 for x in range(5))
print(s)

# 利用tuple生成一个元组.只能使用一次.
print(tuple(s))
print(tuple(s))

# 利用list生成列表.
print(list(s))

s = (x * 3 for x in range(5))
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())
# StopIteration error.
# print(s.__next__())

s = (x * 3 for x in range(5))
print(list(s))


