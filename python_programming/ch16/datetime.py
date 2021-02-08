#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/8
# @Author: Lingchen
# @Prescription: 模块datetime.
#                page_335.
from datetime import datetime

first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
# 2014-07-01 00:00:00.
print(first_date)
