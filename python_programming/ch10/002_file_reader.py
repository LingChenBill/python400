#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/1
# @Author: Lingchen
# @Prescription: 逐行读取文件.
#                page_184.

filename = '../data/pi_digits.txt'

with open(filename) as file_object:
    # 为查看文件的内容,通过对文件对象执行循环来遍历文件中的每一行.
    for line in file_object:
        # 每行末尾都有两个换行符,一个来自于文件,另一个来自于print语句.
        # print(line)
        print(line.rstrip())

