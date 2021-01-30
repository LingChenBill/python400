#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/30
# @Author: Lingchen
# @Prescription: 函数-位置实参.
#                关键字实参.
#                默认值,在形参列表中必须先列出没有默认值的形参,再列出有默认值的实参.


def describe_pet(animal_type, pet_name):
    """显示宠物的信息."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# 输出描述了一只名为Harry的仓鼠.
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# 关键字实参.
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


# 默认值.
def describe_pet2(pet_name, animal_type='dog'):
    """显示宠物的信息, 类型使用默认值."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet2(pet_name='willie')
describe_pet2('willie')
describe_pet2(pet_name='harry', animal_type='hamster')


# TypeError: describe_pet2() missing 1 required positional argument: 'pet_name'.
# 将出现实参不匹配错误.
describe_pet2()
