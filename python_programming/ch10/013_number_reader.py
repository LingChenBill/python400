#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/4
# @Author: Lingchen
# @Prescription: 读取Json文件.
import json

filename = '../data/numbers.json'

with open(filename) as f_obj:
    # 读取json文件内容.
    numbers = json.load(f_obj)

print(numbers)
