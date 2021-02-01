#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/1
# @Author: Lingchen
# @Prescription: 创建一个包含文件各行内容的列表.
#                page_185.

filename = '../data/pi_digits.txt'

with open(filename) as file_object:
    """ open()返回的文件对象只在with代码块内使用.
        要在with代码块外访问文件的内容,可在with代码块内将文件的各行存储在一个列表中.
    """
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
