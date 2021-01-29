#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/29
# @Author: Lingchen
# @Prescription: 列表排序.
import random

# sort默认是升序.
a = [20, 10, 30, 70, 50, 40]
a.sort()
print(a)

# 降序排列.
a.sort(reverse=True)
print(a)
print(id(a))

# 打乱顺序.
random.shuffle(a)
print(a)
print(id(a))

# sorted方法,建新列表的排序.
a = [20, 10, 30, 70, 50, 40]
print(id(a))
print(a)
a = sorted(a)
print(id(a))
print(a)

a = sorted(a, reverse=True)
print(a)

# 返回逆序排列.
a = [20, 10, 30, 70, 50, 40]
print(a)
print(id(a))

# reversed不对原列表做任何修改,只是返回一个逆序排列的迭代器对象.只能使用一次.
c = reversed(a)
print(c)
print(list(c))
print(id(c))

# [].
print(list(c))

c = [20, 10, 30, 70, 50, 40]
# 取最大值,最小值,求各和.
print(max(c))
print(min(c))
print(sum(c))

