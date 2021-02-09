#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/9
# @Author: Lingchen
# @Prescription: 获取国家的国别码.
#                page_346.
from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """ 根据指定的国家, 返回Pygal使用的两个字母的国别码. """

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    # 若没有找到指定的国家,就返回None.
    return None


# print(get_country_code('Albania'))
