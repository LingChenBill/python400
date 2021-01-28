#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/28
# @Author: Lingchen
# @Prescription: 基本运算符.

# 关系运算符可以连用.
a = 4
print(3 < a < 5)

b = 0b11001
c = 0b01000

print(b)
print(c)

# bin()输出二进制.
print(bin(b))
print(bin(c))

# 按位与.
print(bin(b & c))

# 按位异或.
print(bin(b ^ c))

# 左移2位,相当于乘于4.
d = 3
print(d << 2)

# 右移1位,相当于除以2.
e = 8
print(e >> 1)



