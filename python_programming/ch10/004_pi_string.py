#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/1
# @Author: Lingchen
# @Prescription: 使用文件的内容.
#                page_186.

filename = '../data/pi_digits.txt'

with open(filename) as file_object:
    """ open()返回的文件对象只在with代码块内使用.
        要在with代码块外访问文件的内容,可在with代码块内将文件的各行存储在一个列表中.
    """
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    # 删除每一行后面的换行符.
    # pi_string += line.rstrip()
    # 删除每一行的换行符与空格.
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

