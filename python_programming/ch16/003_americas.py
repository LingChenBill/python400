#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/9
# @Author: Lingchen
# @Prescription: 制作世界地图.
#                page_348.
import pygal

wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'
wm.add('North', ['ca', 'mx', 'us'])
wm.add('Central', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

# wm.render()
wm.render_to_file('americas.svg')
