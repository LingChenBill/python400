#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/30
# @Author: Lingchen
# @Prescription: 函数传递任意数量的实参.
#                若要让函数接受不同类型的实参,必须在函数定义中将接纳任意数量实参的形参放在最后.
#                python会优先匹配位置实参和关键字实参,再将余下的实参都收集到最后一个形参中.


def make_pizza(size, *toppings):
    """ 打印顾客点的所有配料.
        形参名*toppings中的星号创建一个名为toppings的空元组,
        并将收到的所有值都封装到这个元组中.
    """
    # print(toppings)
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
