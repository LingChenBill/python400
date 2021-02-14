#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/9
# @Author: Lingchen
# @Prescription: 制作世界人口地图(Json格式).
#                page_343.
#                使用Pygal来设置世界地图的样式.
#                page_353.
#                加亮颜色主题.
#                page_355.
import json
import pygal

from country_codes import get_country_code
from pygal.style import RotateStyle, LightColorizedStyle

# 将数据加载到一个列表中.
filename = '../data/population_data.json'

with open(filename) as f:
    # 将Json数据读取成一个列表.
    pop_data = json.load(f)

# 创建一个包含人口数量的字典.
cc_populations = {}
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
            # print(code + ": " + str(population))
            # 将国家的code,和人口数量存储成一个字典.
            cc_populations[code] = population
        else:
            print('ERROR - ' + country_name)

# 根据人口数量将所有的国家分成三组.
# 少于1000万的, 介于1000万和10亿之间的以及超过10亿的.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 查看每组分别包含多少个国家.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

# 绘制地图.
# wm = pygal.maps.world.World()
# 设置地图样式.
# wm_style = RotateStyle('#336699')

# 设置较亮的主题.
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
# wm.add('2010', cc_populations)

wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population_light.svg')
