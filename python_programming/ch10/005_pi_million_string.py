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

# 检查生日是否在圆周率值中.
birthday = input("Enter your birthday, in the from mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")

