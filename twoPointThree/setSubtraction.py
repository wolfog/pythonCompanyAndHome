# -*-coding:utf-8-*-
# -*- author:wolfog-*-
# purpose: 相当于一个记录程序，用以保存爬取到哪一步。从源url表中拿出地址，然后将请求完成的地
# 址存入详情表中，当发生异常后，只需要将源url地址，减去详情的url地址，就是从哪里开始。
# 只有set才有这种运算。list 没有这种性质。

sourUrl = [item for item in range(1, 40)] + [item for item in range(20, 60)]
urled = [i for i in range(1, 30)] + [i for i in range(20, 40)]
sourSet = set(sourUrl)
urledSet = set(urled)
setResult = sourSet - urledSet
print(setResult)
print(type(setResult))

