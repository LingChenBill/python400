#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/30
# @Author: Lingchen
# @Prescription: 在函数中修改列表.
#                每个函数都应只负责一项具体的工作.

# # 首先创建一个列表,其中包含一些要打印的设计.
# unprinted_designs = ['iphon case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# # 模拟打印每个设计, 直到没有未打印的设计为止.
# # 打印每个设计后,都将其移到列表completed_models中.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#
#     # 模拟根据设计制作3D打印模型的过程.
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)
#
# # 显示打印好的所有模型.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计, 直到没有未打印的设计为止.
    打印每个设计后,都将其移到列表completed_models中.
    :param unprinted_designs:
    :param completed_models:
    :return:
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 模拟根据设计制作3D打印模型的过程.
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# print_models(unprinted_designs, completed_models)
# print(unprinted_designs)

# 切片表示法[:]创建列表的副本.
# unprinted_designs[:]使用的是列表unprinted_designs的副本.而不是unprinted_designs本身.
print_models(unprinted_designs[:], completed_models)
print(unprinted_designs)
show_completed_models(completed_models)
