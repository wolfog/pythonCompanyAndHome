# -*- coding:utf-8 -*-
# _authur_ = 'wolfog'
import re

with open('rentInfo.txt', encoding='utf-8') as dataFile:
    price_list = dataFile.readlines()
    print(price_list.__len__())
    for i in price_list:
        price_num = re.match('\d+', i, re.M)
        if price_num:
            print(price_num.group())
