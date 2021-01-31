#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/31
# @Author: Lingchen
# @Prescription: 序列解包.

x, y, z = (20, 30, 40)
print(x)
print(y)
print(z)

(a, b, c) = (20, 30, 40)
print(a)
print(b)
print(c)

[a, b, c] = [10, 20, 30]
print(a)
print(b)
print(c)

# 序列解包用于字典时,默认是对键进行操作.
s = {'name': 'john', 'age': 19, 'job': 'teacher'}
name, age, job = s
print(name)
print(age)
print(job)

# 对键值对进行操作.
name, age, job = s.items()
print(name)
print(age)
print(job)

# 对值进行操作.
name, age, job = s.values()
print(name)
print(age)
print(job)
