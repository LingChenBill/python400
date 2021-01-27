#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/27
# @Author: Lingchen
# @Prescription: 字符串split()分割与join()合并
import time

a = "to be or not to be"

# 分割.
s = a.split()
print(s)

# 以特定字符分割.
print(a.split('be'))

# 拼接 + .
# 使用字符串拼接符+,会生成新的字符串对象,因此不推荐使用.
print("abc" + "efg")

# 以join拼接,性能优先时,选择join.
print("*".join(s))

b = ""
time_start = time.time()

li = []
for i in range(10000):
    b += "*"

time_end = time.time()
print(b)
print("运算时间:", str(time_end - time_start))

time_start = time.time()

li = []
for i in range(10000):
    li.append("*")

time_end = time.time()
print("".join(li))
print("运算时间:", str(time_end - time_start))

