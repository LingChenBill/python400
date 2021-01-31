#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/31
# @Author: Lingchen
# @Prescription: 字典,键值对的无序可变序列.
#                字典中每个元素都是一个"键值对".
#                字典可以通过"键对象"找到对应的"值对象".
#                字典中,键-不可重复,值-可重复.

# 字典的创建.
a = {'name': 'john',
     'age': 18,
     'job': 'programmer'
     }

print(a)

# 通过dict方式创建字典.
b = dict(name='john',
         age=18,
         job='programmer'
         )
print(b)

c = dict([
    ("name", "john"),
    ("age", 18)
])
print(c)

# 空的字典对象.
d = {}
print(d)

e = dict()
print(e)

# 通过zip()创建字典对象.
k = ['name', 'age', 'job']
v = ['john', 18, 'programmer']
g = dict(zip(k, v))
print(g)

# 通过fromkeys创建值为空的字典.
a = dict.fromkeys(['name', 'age', 'job'])
print(a)




