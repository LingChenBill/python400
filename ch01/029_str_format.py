#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/27
# @Author: Lingchen
# @Prescription: 字符串的格式化.
#                填充与对齐.
#                数字格式化.

a = '名字是:{0},年龄是:{1}'
print(a.format('lc', 28))

a = '名字是:{0},年龄是:{1}, {0}是个好人'
print(a.format('lc', 28))

# 填充与对齐.
# ^:居中, < 左对齐, > 右对齐.
print('{:*>8}'.format(245))

# 保留小数点后两位.
print('{:.2f}'.format(3.1415926))
# 带符号保留小数点后两位.
print('{:+.2f}'.format(3.1415926))

# 不带小数.
print('{:.0f}'.format(2.71828))
# 数字补零(填充左边,宽度为4).
print('{:0>4d}'.format(5))
# 数字补零(填充右边,宽度为4).
print('{:0<4d}'.format(5))

# 以逗号分隔的数字格式.
print('{:,}'.format(1000000))

# 百分比格式.
print('{:.2%}'.format(0.25))

# 指数记法.
print('{:.2e}'.format(1000000000))

# 右对齐.
print('{:10d}'.format(13))
# 左对齐.
print('{:<10d}'.format(13))
# 居中对齐.
print('{:^10d}'.format(13))





