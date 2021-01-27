#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/27
# @Author: Lingchen
# @Prescription: 字符串编码和字符串创建.

# 字符串的默认编码是16位的unicode编码.
print(ord('A'))

print(ord('中'))

print(chr(66))

# 引号创建字符串.

# 可用双引号创建.
a = "I'm a teacher"
print(a)

# 可以单引号创建.
b = 'my name is "TOM"'
print(b)

# 可用三个单引号,创建多行字符串.
resume = '''
    company = "ling"
    age = 29
    name = john
'''
print(resume)

# 字符串的长度.
print(len(resume))
print(resume.__len__())

# 空字符串.
d = ""
print(len(d))
