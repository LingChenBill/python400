#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/2/14
# @Author: Lingchen
# @Prescription: 处理API响应.
#                page_358.
import requests

# 执行API调用并存储响应.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# api_url = 'https://api.github.com/'
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
print('Repositories returned: ', len(repo_dicts))

# 研究第一个仓库.
# repo_dict = repo_dicts[0]
# print("\nKeys: ", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# print("\nSelected information about first repository: ")
# print('Name: ', repo_dict['name'])
# print('Owner: ', repo_dict['owner']['login'])
# print('Stars: ', repo_dict['stargazers_count'])
# print('Repository: ', repo_dict['html_url'])
# print('Created: ', repo_dict['created_at'])
# print('Updated: ', repo_dict['updated_at'])
# print('Description: ', repo_dict['description'])

# 打印每个仓库的信息.
print("\nSelected information about each repository: ")
for repo_dict in repo_dicts:
    print('Name: ', repo_dict['name'])
    print('Owner: ', repo_dict['owner']['login'])
    print('Stars: ', repo_dict['stargazers_count'])
    print('Repository: ', repo_dict['html_url'])
    print('Created: ', repo_dict['created_at'])
    print('Updated: ', repo_dict['updated_at'])
    print('Description: ', repo_dict['description'])
