# -*- coding:utf-8 -*-
# _authur_ = 'wolfog'
# purpose：获得分类项的url地址，并且存入mongoDb中。
# 知识点：python中is 判断是否是一个对象；==判断内容是否相同。
from bs4 import BeautifulSoup
import requests
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client['58']
sortUrl = db['sortUrl']
sortItemUrl = db['sortItemUrl']
sortItemDetail = db['sortItemDetail']
start_url = 'http://bj.58.com/sale.shtml'
url_host = 'http://bj.58.com'


def getSort():
    resq = requests.get(start_url)
    soup = BeautifulSoup(resq.text, 'lxml')
    sortLists = soup.select('li.ym-tab > ul.ym-submnu > li > b > a')  # 注这里需要注意的是标签与大于号一定要有间隔，否则会报错
    for sortList in sortLists:
        print(sortList.getText())
        if not sortList.getText().isspace():  # text为空href就是不重复的值
            sortUrl.insert_one({'sortUrl': url_host + sortList.get('href')})


if __name__ == '__main__':
    getSort()
