#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/2
# @Author: Lingchen
# @Prescription: 附加到文件.
#                'a'以附加模式.
#                page_190.

filename = '../data/programming.txt'

with open(filename, 'a') as file_object:
    # 输出多行时,要在每行中包含换行符.
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

