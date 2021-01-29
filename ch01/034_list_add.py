#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/29
# @Author: Lingchen
# @Prescription: 列表元素的增加和删除.

# 一般只在列表的末尾添加与删除元素.这会大大提高列表的操作效率.
a = [20, 40]
print(id(a))
a.append(80)
print(a)
print(id(a))

# + 操作会创建新的列表对象,涉及大量的复制操作,对于操作大量元素时,会影响效率.
a = a + [50]
print(a)
print(id(a))

# extend方法将目标列表的所有元素添加到本列表的末尾,属于原地操作,不创建新的列表.
a.extend([60, 70])
print(a)
print(id(a))

# insert方法. 可以将指定的元素插入到列表的任意位置,会涉及到大量元素的移动,也不推荐使用.
a.insert(2, 90)
print(a)
print(id(a))

# 乘法扩展.生成一个新的列表.
b = ['python', 100]
print(b)
print(id(b))
b = b * 3
print(b)
print(id(b))

