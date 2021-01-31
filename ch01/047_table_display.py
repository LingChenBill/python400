#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/31
# @Author: Lingchen
# @Prescription: 表格数据使用字典和列表存储,并实现访问.

person_r1 = {'name': '高小一', 'age': 18, 'salary': 30000, 'city': '北京'}
person_r2 = {'name': '高小二', 'age': 19, 'salary': 20000, 'city': '上海'}
person_r3 = {'name': '高小五', 'age': 20, 'salary': 10000, 'city': '深圳'}

tb = [person_r1, person_r2, person_r3]
print(tb)
print(tb[1].get('salary'))

# 打印所有的薪水.
for x in tb:
    print(x.get('salary'))

[print(x.get('salary')) for x in tb]

for x in tb:
    print(x)

[print(x) for x in tb]
