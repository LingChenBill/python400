#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/2
# @Author: Lingchen
# @Prescription: 处理文件异常.
#                page_194.

filename = 'alice.txt'

try:
    # FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'.
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

title = "Alice in Wonderland"
# 方法split()以空格为分隔符将字符串分拆成多个部分,并将这些部分都存储到一个列表中.
print(title.split())


