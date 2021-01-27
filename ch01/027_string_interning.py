#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/27
# @Author: Lingchen
# @Prescription: 字符串驻留机制.
#                对于符合标识符规则的字符串(仅包含下划线,字母和数字)会启用字符串驻留机制.

a = "abd_33"
b = "abd_33"
print(a is b)
print(id(a), id(b))

c = "dd#在"
d = "dd#在"
# True, False.
print(c is d)
print(id(c), id(d))

# 成员操作符.
print("ab" in a)
