#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/14
# @Author: Lingchen
# @Prescription: 使用Pygal可视化仓库.
#                创建一个交互式条形图,条形的高度表示项目获得了多少颗星,
#                单击条形将带你进入项目在Github上的主页.
#                page_363.
import requests
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Github 执行API调用并存储响应.
# url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
url = "https://api.github.com/search/repositories?q=language:vue&sort=stars"

# 使用requests来执行调用,调用get()并将URL传递给它,再将响应对象存储在变量r中.
r = requests.get(url)
# 响应对象包含一个名为status_code的属性.200 -> 请求成功.
print("Status code: ", r.status_code)

# 将API响应存储在一个变量中. json -> 字典.
response_dict = r.json()

# 处理结果.
print(response_dict.keys())
print("Total repositories: ", response_dict['total_count'])

# 探索有关仓库的信息.
repo_dicts = response_dict['items']

# 每个项目的名称,用于给条形加上标签,星数.
# names, stars = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    # 存储星数与描述.提示工具条.
    # Pygal根据与键'xlink'相关联的URL将每个条形都转换为活跃的链接.
    # AttributeError: 'NoneType' object has no attribute 'decode'.
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# 可视化.
# 设置深蓝色样式.
my_style = LS('#333366', base_style=LCS)

# 改进Pygal图表.定制图表样式.
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False

# 设置图表标题,副标签和主标签的字体大小.
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18

my_config.truncate_label = 15
# 隐藏图表中的水平线.
my_config.show_y_guides = False
my_config.width = 1000

# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart = pygal.Bar(my_config, style=my_style)

chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

# chart.add('', stars)

# 添加工具提示.
chart.add('', plot_dicts)

# chart.render_to_file('python_repos_plot.svg')
# chart.render_to_file('python_repos_xlink.svg')
chart.render_to_file('vue_repos_xlink.svg')

