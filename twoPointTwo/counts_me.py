# -*-coding:utf-8-*-
# -*- author:wolfog-*-
# purpose:过一段时间去数据库看下有多少条数据了
import time

from channel_extract_me import sortItemUrl
from channel_extract_me import sortItemDetail


def getSortItemUrlCount():
    print(sortItemUrl.find().count())
    time.sleep(5)


def getsortItemDetailCount():
    print(sortItemDetail.find().count())
    time.sleep(5)


while True:
    getsortItemDetailCount()
    # getSortItemUrlCount()
