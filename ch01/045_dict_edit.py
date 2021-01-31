#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/31
# @Author: Lingchen
# @Prescription: 字典元素的添加,修改,删除.

# 字典.
a = {'name': 'John', 'age': 18, 'job': 'programmer'}

# 添加元素.
a['address'] = '西二旗'
print(a)

# 会覆盖原有的健值对.
a['age'] = 20
print(a)

# 使用update()将新字典中所有键值对全部添加到旧字典对象上.若有key,则覆盖.
b = {'name': 'Tom', 'age': 39, 'job': 'programmer', 'money': 30000}
a.update(b)
print(a)

# 字典的元素的删除.
del(a['name'])
print(a)

c = a.pop('money')
print(c)
print(a)

# 字典清空.
a.clear()
print(a)

# 随机删除和返回该键值对.
b = {'name': 'Tom', 'age': 39, 'job': 'programmer', 'money': 30000}
b.popitem()
print(b)
