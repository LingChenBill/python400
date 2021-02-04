#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/4
# @Author: Lingchen
# @Prescription: 测试函数.
#                page_206.


def get_formatted_name(first, last, middle=''):
    """ Generate a neatly formatted full name. """

    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()

