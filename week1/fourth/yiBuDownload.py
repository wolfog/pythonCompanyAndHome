# -*- coding:utf-8 -*-
# _authur_ = 'wolfog'
# 获取异步加载的数据（这里的异步是指首页加载第一次请求和上拉加载更多不是一个网址，这个异步是指相对于第一次请求的网址非一致性）
# 做爬虫就是要多观察，这里才发现了文章的url链接组成形式，当class 的值为article时，以一种格式，等于news是另外一种格式
import requests


def onePage(id):
    url = 'https://api.yii.dgtle.com/v2/index?token=&perpage=14&page={}'.format(id)
    resq = requests.get(url).text
    # eval 将一个字符串转化为一个字典
    test = eval(resq)
    for i in test['list']:
        print(i['pic'])
        print(i['title'])
        if (i['class'] == "article"):
            print("http://www.dgtle.com/article-{}-1.html".format(i['aid']))
        if (i['class'] == "news"):
            print('http://news.dgtle.com/thread-{}-1-1.html'.format(i['tid']))
        print()


for i in range(0, 9):
    onePage(i)
