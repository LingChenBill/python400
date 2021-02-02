#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/2
# @Author: Lingchen
# @Prescription: 使用多个文件.
#                page_196.


def count_words(filename):
    """ 计算一个文件大致包含多少个单词. """

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # 计算文件大致包含多少个单词.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


# filename = '../data/alice.txt'
# count_words(filename)

filenames = ['../data/alice.txt', '../data/siddhartha.txt', '../data/moby_dick.txt', '../data/little_women.txt']
for filename in filenames:
    count_words(filename)

