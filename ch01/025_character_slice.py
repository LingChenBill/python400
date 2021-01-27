#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/27
# @Author: Lingchen
# @Prescription: 字符串切片slice操作.
#                [起始偏移量start, 终止偏移量end, 步长step].
#                左闭右开.

s = 'abcdefghijklmn'
print(s)
print(s[2])

# slice切片.左闭右开,默认步长为1.
print(s[1:5])

# 步长为2.
print(s[1:5:2])

print(s[:])

print(s[2:])

print(s[:3])

# 操作数为负数时,逆序, 左闭右开.
print(s[-3:-1])

print(s[-3:])

print(s[::-1])

# 起始偏移量与终止偏移量不在字符串范围内,也不会报错.
print(s[2:300])

