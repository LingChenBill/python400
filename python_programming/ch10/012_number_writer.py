#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/4
# @Author: Lingchen
# @Prescription: 存储数据.
#                使用json.dump()和json.load().
#                page_199.
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = '../data/numbers.json'

with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
