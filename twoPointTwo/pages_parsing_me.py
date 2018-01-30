# -*- coding:utf-8 -*-
# _authur_ = 'wolfog'
# purpose：两个任务。一：根据sort地址，拿到本大类下所有的商品的url,像代码那样，这个类就封装成一个方法，比较清晰
# (http://bj.58.com/shouji/pn30/)。
from multiprocessing.pool import Pool

import requests
import time
from bs4 import BeautifulSoup
from channel_extract_me import sortItemUrl
from channel_extract_me import sortItemDetail


def getAllUrlOfSort(sortUrl):
    resq = requests.get(sortUrl)
    soup = BeautifulSoup(resq.text, 'lxml')
    sortItemUrls = soup.select('tr.zzinfo > td.img > a')
    for item in sortItemUrls:
        sortItemUrl.insert_one({"sortItem": item.get('href')})


def getDetail(
        url):  # 总共有359个是58同城的地址，所以很可能会出现359个请求不到消息的地址，42336正常                        # 经过分析url地址有两种格式。跳到转转和跳到58同城。需要分开讨论。
    time.sleep(1)
    try:
        resq = requests.get(url)
        soup = BeautifulSoup(resq.text, 'lxml')
        if "//zhuanzhuan" in url:  # 转转的地址
            titles = soup.select('div.box_left_top > h1')
            prices = soup.select('span.price_now > i')
            scanNums = soup.select('p.info_p > span.look_time')
            areas = soup.select('div.palce_li > span > i')
            urlSource = soup.select('#img_smalls > li.hover > img')  # 住“#”表示的是img_small为id选择器，三个图片src属性
            urls = []
            for item in urlSource:
                urls.append(item.get('rel'))
        else:  # 58同城
            titles = soup.select('div.col_sub.mainTitle > h1')
            prices = soup.select('div.su_con > span.price.c_f50')
            scanNums = soup.select('#totalcount')  # 这个数字也有问题，为什们请求回来的时候就是0，那么真正的浏览次数呢
            areaSource = soup.select('span.c_25d > a')  # 两个地址拼接
            urlSource = soup.select('#img_smalls > li > img')  # 住“#”表示的是img_small为id选择器，,src拼接
            areas = []
            urls = []
            for item in areaSource:
                areas.append(item.getText())
            for itemUrl in urlSource:
                urls.append(itemUrl.get('src'))
        for title, price, scanNum, area, url in zip(titles, prices, scanNums, areas, urls):
            print({'title': title.getText(), 'price': price.getText(), 'scanNum': scanNum.getText(),
                   'area': area.getText(), 'url': url, 'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())})
            sortItemDetail.insert_one(
                {'title': title.getText(), 'price': price.getText(), 'scanNum': scanNum.getText(),
                 'area': area.getText(), 'url': url, 'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())})
    except Exception:
        with open('exception.txt', 'a') as file:
            file.write(url + '\n')


if __name__ == '__main__':  # 58的格式关于title的都不一样，难道还要分情况讨论
    pool = Pool()
    urlLists = []
    for sortItem in sortItemUrl.find():
        urlLists.append(sortItem['sortItem'])
    pool.map(getDetail, urlLists)
