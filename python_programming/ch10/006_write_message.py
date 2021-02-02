#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/2
# @Author: Lingchen
# @Prescription: 写入空文件.
#                open的第二个实参: 'w'以写入模式打开文件.
#                'r'以指定读取模式.
#                'r+'读取和写入文件的模式.
#                'a'以附加模式.
#                省略了模式实参,默认以只读模式打开.
#                page_189.

filename = '../data/programming.txt'

with open(filename, 'w') as file_object:
    # 输出多行时,要在每行中包含换行符.
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

