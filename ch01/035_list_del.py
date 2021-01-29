#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/29
# @Author: Lingchen
# @Prescription: 列表元素的删除.

a = [10, 20, 30]
print(a)

# 删除列表指定位置的元素.
del a[1]
print(a)

# pop删除并返回指定位置元素.
a = [10, 20, 30]
print(a)
a.pop(1)
print(a)

a.pop()
print(a)

# remove删除首次出现的指定元素,若不存在该元素则出现异常.
a = [10, 20, 30, 40, 50, 40, 60, 70]
print(a)
a.remove(40)
print(a)

# ValueError: list.remove(x): x not in list.
# a.remove(100)


