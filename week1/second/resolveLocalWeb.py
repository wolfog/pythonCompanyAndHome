# -*- coding:utf-8 -*-
# _authur_ = 'wolfog'

# 使用open方法读取本地网页；
# 用beautiful解析，得到soup文件；
# soup.select("需要selector的路径（可以有selector和Xpath路径）")；注：这里使用的是selector。这里可能需要获取父类，比如获取的cate（子类路径删除掉），或者所有的子类将nth-of-type(1)全去掉（那就将第几个子类删除掉）
# 拿到所有标题，评分，描述，图片，类别，并将这些值装入一个字典中，将这个字典装入一个结合中
# 遍历结合，根据筛选条件从而打印出title和cate



from bs4 import BeautifulSoup

listObj = []
with open('D:\麻瓜编程项目文件\课程源码及作业参考答案\Plan-for-combating-master\week1/1_2/1_2code_of_video\web/new_index.html', 'r',
          encoding='utf-8') as wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')
    imgs = Soup.select('body > div.main-content > ul > li > img')
    titles = Soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    cates = Soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info')
    descs = Soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    rates = Soup.select('body > div.main-content > ul > li > div.rate > span')

for img, title, cate, desc, rate in zip(imgs, titles, cates, descs, rates):
    obj = {'img': img.get('src'), 'title': title.get_text(), 'desc': desc.get_text(),
           'cate': list(cate.stripped_strings), 'rate': rate.get_text()}
    listObj.append(obj)

for i in listObj:
    if (float(i['rate']) > 3):
        print(i['title'], i['desc'])
