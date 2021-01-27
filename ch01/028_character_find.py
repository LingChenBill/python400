#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/27
# @Author: Lingchen
# @Prescription: 字符串常用查找方法.
#                去除首尾信息.
#                大小写转换.
#                格式排版.

s = '''I'm a python leanring member.
Day day up.
Continue to practice.
'''

# 字符串长度.
print(len(s))

# 以指定字符串开头.
print(s.startswith('I'))

# 以指定字符串结尾.
print(s.endswith('e.\n'))

# 第一次出现指定字符串的位置.
print(s.find('Day'))

# 最后一次出现指定字符串的位置.
print(s.rfind('up.'))

# 指定字符串出现了几次.
print(s.count('e'))

# 所有字符全是字母或数字.
print(s.isalnum())
print(s.isalpha())

print("abc123".isalnum())

# 去除首尾信息.
t = '  abc  '
print(t.strip())
print(t.lstrip())
print(t.rstrip())

l = '****abcd***'
print(l.rstrip('*'))

# 大小写转换.
a = 'i am is a python learning member.'
print(a.capitalize())

# 格式排版.
b = 'xyz'
print(b.center(10, '*'))

print(b.center(10))

print(b.ljust(10, '*'))

print(''.isspace())
print('\t\n'.isspace())
