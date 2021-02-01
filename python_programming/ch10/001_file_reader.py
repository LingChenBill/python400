#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/1
# @Author: Lingchen
# @Prescription: 读取整个文件.
#                在Linux与os x系统中,文件路径中使用斜杠 /
#                在windows系统中,文件路径中使用反斜杠 \
#                page_182.

# 关键字with在不再需要访问文件后将其关闭.
with open('../data/pi_digits.txt') as file_object:
    # 读取整个文件文本.
    contents = file_object.read()
    print(contents)
