#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/8
# @Author: Lingchen
# @Prescription: 分析CSV文件头.
#                page_331.
import csv

from matplotlib import pyplot as plt
from datetime import datetime

# filename = '../data/sitka_weather_07-2014.csv'
# 更多的气温数据.
# filename = '../data/sitka_weather_2014.csv'
# 分析异常数据.
filename = '../data/death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    # 查看文件的标题行.
    header_row = next(reader)
    # print(header_row)

    # 将列表中的每个文件头及其位置打印出来.
    # 对列表调用了enumerate()来获取每个元素的索引及其值.
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 读取每天的最高气温.
    # 从文件中获取日期和最高气温.
    # dates, highs = [], []
    dates, highs, lows = [], [], []
    # 遍历数据行.
    for row in reader:
        # 将索引1处的数据附加到highs末尾.-> 每天的最高气温(1列).
        # highs.append(row[1])

        # ValueError: invalid literal for int() with base 10: ''
        # 处理异常数据.
        try:
            # 日期.
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            # 将气温的字符串转换成了数字.
            high = int(row[1])
            # 最低气温.
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data!')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # print(highs)

    # 根据数据绘制图形.
    fig = plt.figure(dpi=128, figsize=(10, 6))
    # 绘制折线图,显示了阿拉斯加锡特卡2014年7月每天的最高气温.
    # plt.plot(highs, c='red')
    # 最高气温.
    # plt.plot(dates, highs, c='red')
    # 最低气温.
    # plt.plot(dates, lows, c='blue')

    # 给图表区域着色.
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    # 填充色. alpha值为0表示完全透明,1(默认设置)表示完全不透明.
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置图形的格式.
    # plt.title("Daily high temperatures, July 2014", fontsize=24)
    # plt.title("Daily high temperatures - 2014", fontsize=24)
    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16)

    # 绘制斜的日期标签,以免它们彼此重叠.
    fig.autofmt_xdate()

    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


