#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/31
# @Author: Lingchen
# @Prescription: 类.
#                在Python,首字母大写的名称指的是类.


class Dog():
    """一次模拟小狗的简单测试."""

    def __init__(self, name, age):
        """ 初始化属性name和age.
            实参self.每个与类相关联的方法调用都自动传递实参self,
            它是一个指向实例本身的引用,让实例能够访问类中的属性和方法.
            self.变量被关联到当前创建的实例.
        """
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# 调用方法.
my_dog.sit()
my_dog.roll_over()

# 可安需求根据类创建任意数量的实例.
your_dog = Dog('lucy', 3)
print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
