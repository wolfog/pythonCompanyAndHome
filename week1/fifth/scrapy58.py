# -*- coding:utf-8 -*-
# _authur_ = 'wolfog'

import time

import requests
# 爬取58第一页，所有来自转转的信息的类目，标题，价格，区域,浏览量（不过这个跟视频上说的不一样，他直接就可以加载出来，完全不是js加载）
from bs4 import BeautifulSoup

a = 0


def getOneDetail(url_detail):
    time.sleep(2)
    resq_detail = requests.get(url_detail)
    soup_detail = BeautifulSoup(resq_detail.text, 'lxml')
    types = soup_detail.select('#nav > div > span:nth-of-type(4) > a')
    titles = soup_detail.select(
        'body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.box_left_top > h1')
    prices = soup_detail.select(
        'body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.price_li > span > i')
    places = soup_detail.select(
        'body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.palce_li > span > i')
    browses = soup_detail.select(
        'body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.box_left_top > p > span.look_time')
    for type, title, price, place, browse in zip(types, titles, prices, places, browses):
        print(a)
        print(type.getText())
        print(title.getText())
        print(price.getText())
        print(place.getText())
        print(browse.getText())
        print('====================================================================================================')
        with open('58.txt', 'a', encoding='utf-8') as file:
            file.write(str(
                a) + type.getText() + "\n" + title.getText() + "\n" + price.getText() + "\n" + place.getText() + "\n" + browse.getText())
            file.flush()


home_url = 'http://bj.58.com/pbdn/0/'

resq = requests.get(home_url)
soup = BeautifulSoup(resq.text, 'lxml')
label_list = ['#infolist > div:nth-of-type(4) > table > tbody > tr:nth-of-type({}) > td.t > a'.format(lc) for lc in
              range(1, 3)]
detail_urlList = []
for i in label_list:
    url_list = soup.select(i)
    for j in url_list:
        detail_urlList.append(j.get("href"))
for k in detail_urlList:
    a += 1
    getOneDetail(k)
