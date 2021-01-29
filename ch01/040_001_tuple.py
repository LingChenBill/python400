#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/29
# @Author: Lingchen
# @Prescription: 元组tuple.
#                列表属于可变序列,可以任意修改列表中的元素.
#                元组属于不可变序列,不能修改元组中的元素.
#                元组没有增加,修改,删除元素相关的方法.

# 元组的创建.
a = (10, 20, 30)
print(a)
print(type(a))

# 只有一个元素的元组.
c = (20,)
print(c)

# 不写逗号是,只是一个数字.
d = (20)
print(d)

# 通过tuple()创建.将其它类型的元素转换成元组.
b = tuple([10, 20, 30])
print(b)
print(type(b))

e = tuple(range(3))
print(e)

f = tuple("abc")
print(f)
print(type(f))
