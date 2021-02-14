#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/10
# @Author: Lingchen
# @Prescription: 在世界地图上呈现数字数据.
#                page_349.
import pygal

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'
# 传递一个字典而不是列表.
# Pygal根据数字自动给不同国家着以深浅不一的颜色.(人口最少-颜色最浅,人口最多-颜色最深).
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')

