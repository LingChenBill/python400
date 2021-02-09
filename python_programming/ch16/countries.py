#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/9
# @Author: Lingchen
# @Prescription:
from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
