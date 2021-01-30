#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/30
# @Author: Lingchen
# @Prescription: 函数返回值, 可以返回一个值或一组值.


# def get_formatted_name(first_name, middle_name, last_name):
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# musician = get_formatted_name('john', 'lee', 'hooker')

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
