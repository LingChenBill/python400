#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/29
# @Author: Lingchen
# @Prescription: 二维列表.

# 列表中可以嵌套列表.
a = [
    ["高小一", 18, 30000, "北京"],
    ["高小二", 19, 20000, "深圳"],
    ["高小五", 20, 10000, "上海"],
]

print(a)

# 通过列表索引获取列表中的元素.
print(a[0])
print(a[0][1])

# 循环遍历2维列表.
for m in range(3):
    for n in range(4):
        print(a[m][n], end='\t')
    # 打印完一行,换行.
    print()
