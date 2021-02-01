#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/1
# @Author: Lingchen
# @Prescription: Python标准库.
#                记录被调查者参与调查的顺序.
#                类名应采用驼峰命名法,即将类名中的每个单词的首字母都大写.而不使用下划线.
#                实例名和模块名都采用小写格式.并在单词之间加上下划线.
#                page_178.
from collections import OrderedDict

# 创建一个空的有序字典.
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

