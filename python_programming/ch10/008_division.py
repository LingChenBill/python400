#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/2
# @Author: Lingchen
# @Prescription: 处理异常.
#                异常是使用try-catch代码块来处理的.来处理异常时该怎么办.
#                page_191.

# ZeroDivisionError: division by zero.
# print(5 / 0)

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me two number, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
