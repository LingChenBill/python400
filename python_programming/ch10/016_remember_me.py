#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/4
# @Author: Lingchen
# @Prescription: 输入,获取用户.
#                page_201.
import json

# 如果以前存储了用户名,就加载它.
# 否则,就提示用户输入用户名并存储它.

filename = '../data/username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you com back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
