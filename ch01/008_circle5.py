#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/1/27
# @Author: Lingchen
# @Prescription: 绘制奥运五环.
import turtle

# 圆环的宽度.
turtle.width(10)
# 画第一个圆环.
turtle.color("blue")
turtle.circle(50)

# 画至某一个点(去掉其中的线).
turtle.penup()
turtle.goto(120, 0)
turtle.pendown()
# 画第二个圆环.
turtle.color("black")
turtle.circle(50)

turtle.penup()
turtle.goto(240, 0)
turtle.pendown()
# 画第三个圆环.
turtle.color("yellow")
turtle.circle(50)

turtle.penup()
turtle.goto(60, -50)
turtle.pendown()
# 画第四个圆环.
turtle.color("red")
turtle.circle(50)

turtle.penup()
turtle.goto(180, -50)
turtle.pendown()
# 画第五个圆环.
turtle.color("green")
turtle.circle(50)
