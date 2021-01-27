#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/27
# @Author: Lingchen
# @Prescription: 数字转型字符串.
#                使用[]提取字符.
#                replace替换.

# 把数字转型为字符串.
print(str(5.30))
print(str(314))

# 把bool转换为字符串.
print(str(True))

# 使用[]提取字符.
s = 'I am a pythoner'
# 正向搜索.
print(s[0])
print(s[3])

# 反向搜索.
print(s[-1])

# IndexError: string index out of range.
# print(s[-20])

print(s[len(s) - 1])

# 字符串替换.

# 字符串不可修改.
# TypeError: 'str' object does not support item assignment.
# s[1] = 'b'
# print(s)

# replace重新生成一个对象.
t = s.replace('a', 'A')
print(s)
print(t)
