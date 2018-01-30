# -*- coding:utf-8 -*-
# _authur_ = 'wolfog'
# 爬取一个本地网站，并且统计图片地址，价格，标题，评分量，评分星级（难点在于如果统计评分星级）
from bs4 import BeautifulSoup

with open(
        "D:/麻瓜编程项目文件/课程源码及作业参考答案/Plan-for-combating-master/week1/1_2/1_2answer_of_homework/1_2_homework_required/index.html",
        'r') as webPage:
    Soup = BeautifulSoup(webPage, "lxml")
    img1 = Soup.select(
        'body > div:nth-of-type(2)> div > div.col-md-9 > div:nth-of-type(2)> div:nth-of-type(1)> div > img')
    img2 = Soup.select(
        'body > div:nth-of-type(2)> div > div.col-md-9 > div:nth-of-type(2)> div:nth-of-type(2)> div > img')
    img3 = Soup.select(
        'body > div:nth-of-type(1)> div > div.col-md-9 > div:nth-of-type(2)> div:nth-of-type(3)> div > img')
    print(img1)
    print(img2)

    # body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > img
    print(img3)

# body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > img
#     body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(2) > div > img
# body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(3) > div > img
