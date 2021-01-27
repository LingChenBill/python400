#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/27
# @Author: Lingchen
# @Prescription: 转义字符.

# 转义字符\
a = 'I\nlove\nu'
print(a)

b = 'I\'m a teacher'
print(b)

# 换行符\.
c = 'I am a \
    teacher'
print(c)

# 字符串拼接 + .
print("aa" + "bb")
print("aa" "bb")

# 字符串复制 * .
d = 'lc' * 3
print(d)

# 不换行打印.
print('python')
print('python', end='')
print('python', end='\t')
print('python')

# 从控制台读取字符串.
name = input('请输入名字:')
print(name)




