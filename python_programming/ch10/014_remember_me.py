#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/4
# @Author: Lingchen
# @Prescription: 存储用户的名字.
import json

username = input("What is your name? ")

filename = '../data/username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + '!')

