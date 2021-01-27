#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/27
# @Author: Lingchen
# @Prescription: 同一运算符.

a = 100000022
b = 100000022

# is是判断两个标识符是不是引用同一个对象.
# 若为True, 有缓存问题.
print(a is b)
# == 用于判断引用变量引用对象的值是否相等.
print(a == b)

c = -600
d = -600
print(c is d)

