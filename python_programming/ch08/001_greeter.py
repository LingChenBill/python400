#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/30
# @Author: Lingchen
# @Prescription: 打印问候语的简单函数.


# def greet_user():
#     """显示简单的问候语"""
#     print("Hello!")
# greet_user()

def greet_user(username):
    """显示简单的问候语, title()内置函数,开头大写,其余小写."""
    print("Hello, " + username.title() + "!")


greet_user('jesse')

