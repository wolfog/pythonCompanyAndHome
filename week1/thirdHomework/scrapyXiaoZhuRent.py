# -*- coding:utf-8 -*-
# _authur_ = 'wolfog'
# 爬取小猪短租的信息
# 和官方答案对比后，发现我的思路使用的是list.get(0)学会使用zip函数
from bs4 import BeautifulSoup
import requests
import time

url_host = 'http://sz.xiaozhu.com/fangzi/'
id_list = []


def getOneIdDetail(url):
    """
获取一个id的详情
    :param url:
    """
    # try:
    resq = requests.get(url)
    soup = BeautifulSoup(resq.text, 'lxml')
    # 为什么添加上body就无法得到值呢
    titles = soup.select(' div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')  # 为什么添加上body就无法得到值呢
    lacations = soup.select(' div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')  # 为什么添加上body就无法得到值呢
    # pics = soup.select('div[id="imgMouseCusor"] > img[id="curBigImage"]')#为什么添加前面的父布局就
    pics = soup.select('img[id="curBigImage"]')
    prices = soup.select('#pricePart > div.day_l > span')
    landlord_pics = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    landlord_gender = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    landlord_name = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')

    with open('rentInfo.txt', 'a', encoding='utf-8') as infoFile:
        infoFile.write(
            titles[0].getText() + "\n" + lacations[0].getText() + "\n" + prices[0].getText() + "\n" + pics[0].get(
                'src') +
            # "\n" + landlord_pics[0].get('src') + "\n" + landlord_name[0].get('title') + "\n" + review_landlord[
            #     0].text + "\n"
            "\n" + landlord_pics[0].get('src') + "\n" + landlord_name[0].get('title') + "\n"
        )
        # review_consumer[0].text暂时不写
        print(titles[0].getText() + "\n" + lacations[0].getText() + "\n" + prices[0].getText() + "\n" + pics[0].get(
            'src'))

        for i in landlord_gender[0].get('class'):
            if str(i).endswith('1'):
                infoFile.write('女' + "\n")
                print('女' + "\n")
            else:
                infoFile.write("男" + "\n")
                print("男" + "\n")
        infoFile.write("=============================================================================" + '\n')
        infoFile.flush()
        print("=============================================================================")


def getOnePageId(page):
    """
获取一页的所有id
    """
    url_home = url_host + 'search-duanzufang-p{}-0/'.format(page)
    print(url_home)
    soup_home = BeautifulSoup(requests.get(url_home).text, 'lxml')
    test = soup_home.select("#page_list > ul > li")
    for j in test:
        list_page = str(j.get('lodgeunitid')).split("_")
        id_list.append(list_page[list_page.__len__() - 1])


def getAllID():
    """
    获取所有的id
    """
    for k in range(1, 14):
        getOnePageId(k)


def getOneIDDetail(id):
    """
    获得一页的详情
    """
    time.sleep(2)  # 防止id被封
    url_onePage = url_host + str(id) + ".html"
    print(url_onePage)
    getOneIdDetail(url_onePage)


getAllID()
for id in id_list:
    getOneIDDetail(id)
