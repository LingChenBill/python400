#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/27
# @Author: Lingchen
# @Prescription: 链式赋值,同一个对象赋值给多个变量.

# 链式赋值.
x = y = 123
print(x)
print(y)

# 系列数据赋值给对应相同个数的变量(个数必须保持一致).
a, b, c = 10, 20, 30
print(a)
print(b)
print(c)

# 使用系列解包赋值实现变量交换.
a, b = 50, 60
a, b = b, a
print(a)
print(b)

# python不支持常量,值可以改变.只能在逻辑上不做修改.
MAX_SPEED = 120
print(MAX_SPEED)

MAX_SPEED = 150
print(MAX_SPEED)
