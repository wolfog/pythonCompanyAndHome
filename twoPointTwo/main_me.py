# -*- coding:utf-8 -*-
# _authur_ = 'wolfog'
# purpose：启动程序的，

import time
from multiprocessing import Pool

from channel_extract_me import sortUrl
from pages_parsing_me import getAllUrlOfSort


def allUrlofSort(sortUrl):
    for page in range(1, 100):
        urlWithPage = sortUrl['sortUrl'] + "pn{}/".format(page)
        time.sleep(1)
        try:
            getAllUrlOfSort(urlWithPage)
        except(Exception, EOFError):
            print(urlWithPage)


if __name__ == '__main__':
    pool = Pool()  # 调动多进程进行执行，验证过结果。
    pool.map(allUrlofSort, sortUrl.find())
