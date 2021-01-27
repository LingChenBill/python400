#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/27
# @Author: Lingchen
# @Prescription: 可变字符串.
import io

s = 'hello python'
sio = io.StringIO(s)
print(sio)
print(sio.getvalue())

# 原地修改字符串.
print(sio.seek(7))
print(sio.write("python"))

print(sio.getvalue())
