#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/27
# @Author: Lingchen
# @Prescription: python中,除了10进制,还有二进制,八进制,十六进制.

print(12)

# 二进制:0b或0B.
print(0b101)

# 八进制:0o或0O.
print(0o10)

# 十六进制:0x或0X.
print(0xf)
print(0xff)

print(0x10)

# 使用int()实现类型转换,去掉小数部分.
print(int(3.1415))
print(int(3.999))

print(int(False))

# ValueError: invalid literal for int() with base 10: '123abc'
# print(int("123abc"))
