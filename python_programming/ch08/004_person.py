#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/30
# @Author: Lingchen
# @Prescription: 函数返回字典.
#                函数可返回任何类型的值,包括列表和字典等较复杂的数据结构.


def build_person(first_name, last_name, age=''):
    """返回一个字典,其中包含有关一个人的信息."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix')
print(musician)

musician = build_person('jimi', 'hendrix', age=27)
print(musician)


