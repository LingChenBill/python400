#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/30
# @Author: Lingchen
# @Prescription: 函数使用任意数量的关键字实参.
#                预先不知道传递给函数的会是什么样的信息,
#                在这种情况下,可将函数编写成能够接受任意数量的键-值对.


def build_profile(first, last, **user_info):
    """ 创建一个字典,其中包含我们知道的有关用户的一切.
        **user_info中的两个星号创建一个名为user_info的空字典,
        并将收到的所有名称-值对都封装到这个字典中.
    """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value

    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)
