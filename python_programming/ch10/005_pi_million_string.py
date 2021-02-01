#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/1
# @Author: Lingchen
# @Prescription: 包含一百万位的大型文件.
#                page_187.

filename = '../data/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:52] + "...")
print(len(pi_string))
