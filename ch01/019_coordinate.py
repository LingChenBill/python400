#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/27
# @Author: Lingchen
# @Prescription: 定义多点坐标,绘制路径,并计算起始点和终点距离.
import turtle
import math

# 定义多个点的坐标.
x1, y1 = 100, 100
x2, y2 = 100, -100
x3, y3 = -100, -100
x4, y4 = -100, 100

# 绘制拆线.
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()

turtle.goto(x2, y2)
turtle.goto(x3, y3)
turtle.goto(x4, y4)

# 计算起始点与终点距离.
distance = math.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
turtle.write(distance)
print(distance)
