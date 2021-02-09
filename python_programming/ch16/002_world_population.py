#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/9
# @Author: Lingchen
# @Prescription: 制作世界人口地图(Json格式).
#                page_343.
import json

from country_codes import get_country_code

# 将数据加载到一个列表中.
filename = '../data/population_data.json'

with open(filename) as f:
    # 将Json数据读取成一个列表.
    pop_data = json.load(f)

# 打印每个国家的2010年的人口数量.
for pop_dict in pop_data:
    # 遍历pop_data中的每个元素,元素是一个字典.
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # population = pop_dict['Value']
        # print(country_name + ": " + population)

        # 将人口数量的字符串转换成数字值.
        # ValueError: invalid literal for int() with base 10: '1127437398.85751'.
        # population = int(pop_dict['Value'])

        # 将字符串转换成小数,再用int丢弃小数部分.
        population = int(float(pop_dict['Value']))
        # print(country_name + ": " + str(population))

        code = get_country_code(country_name)
        if code:
            print(code + ": " + str(population))
        else:
            print('ERROR - ' + country_name)

