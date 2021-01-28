#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/28
# @Author: Lingchen
# @Prescription: 列表.
#                推导式生成列表.

# 列表中值可以是任何类型.
a = [20, 30, 40, "python"]
print(a)

# 获取列表中的值.
print(a[3])

# 列表增加元素.
b = []
b.append(50)
print(b)

a.append("hello")
print(a)

c = list()
print(c)

d = list("python")
print(d)

# 创建整数列表.
print(range(10))

e = range(10)
print(type(e))

print(list(e))

# TypeError: range expected 0 argument, got 0.
# print(range())

# 通过list()获取列表.
print(list(range(10)))
print(list(range(0, 10, 1)))
print(list(range(3, -10, -1)))

# 推导式生成列表.

# 循环创建多个元素.
f = [x * 2 for x in range(5)]
print(f)

g = [x * 2 for x in range(100) if x % 9 == 0]
print(g)
