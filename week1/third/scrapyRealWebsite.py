# -*- coding:utf-8 -*-
# _authur_ = 'wolfog'
# 爬取一个真实网站
# 爬取所有的图片，题目，分类
# 爬取我收藏的
# pc端爬不上了，爬移动端（伪造）
# 爬取京都所有的宾馆图片，名字，价格，点评数

from bs4 import BeautifulSoup
import requests

url = 'https://www.tripadvisor.cn/Hotels-g298564-Kyoto_Kyoto_Prefecture_Kinki-Hotels.html#apg=f045ac62a2db4d6f8060ad50236ac00a&ss=C1F64DB76A003964711F223C5F6855FB'
data = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
    'Cookie': 'TAUnique=%1%enc%3AzmlG6vDWW0bovgaOPHdym6SpXhaeNcFaY0%2BmUPC6j6hmBG5oxLgiyQ%3D%3D; BEPIN=%1%15fc03114c8%3Bbak09c.daodao.com%3A10023%3B; ServerPool=A; TASSK=enc%3AAAiI3RJBukPvzHZo2IjbJNBpYgLbFiM8gwUX6Lwzt9PSQspKyExlvqJx33olZy%2BjPUzoF2qU1BI1jKMCvW%2BVLe18QV85%2FK9%2Foq5D%2FAoF%2BFm5lYIQLTXYSSCzGZA86kCLZA%3D%3D; VRMCID=%1%V1*id.12019*llp.%2F*e.1511362765680; CommercePopunder=SuppressAll*1510757983612; __gads=ID=a16fc93c8aae969e:T=1510757986:S=ALNI_MZEuWWk9DwFkL_Yw_oNT-zt-MOFWw; _smt_uid=5a0c5666.2875d5ce; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C4%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7Cmds%2C1510758289606%2C1510844689%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; ki_t=1510758255091%3B1510758255091%3B1510759605162%3B1%3B8; ki_r=; TAReturnTo=%1%%2FHotels-g298564-Kyoto_Kyoto_Prefecture_Kinki-Hotels.html; roybatty=TNI1625!AGt8iYgYOuMUlBtPIGc5jFuLWzRmsTsw0XCjPmad8m5izQ64XnoAabFAHqcX1JhBzn05KwZX4cwEb6SYQQK7bTa7tTGp4Lcc24gqSobJh7P8NIDzcc5kqfxhKHauzP2ly84rdJ3tHIfefNhOTwTY5I%2BABQ9LYGmDCUOt2DYQmo58%2C1; _ga=GA1.2.515086315.1510757968; _gid=GA1.2.1980042938.1510757968; TASession=%1%V2ID.C1F64DB76A003964711F223C5F6855FB*SQ.129*MC.12019*LR.https%3A%2F%2Fwww%5C.baidu%5C.com%2Fs%3Fie%3DUTF-8%26wd%3Dtripadvisor*LP.%2F*LS.DemandLoadAjax*GR.92*TCPAR.54*TBR.31*EXEX.28*ABTR.14*PHTB.7*FS.24*CPU.13*HS.priceLow*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*LF.zhCN*FA.1*DF.0*MS.-1*RMS.-1*FLO.298566*TRA.true*LD.298564; TATravelInfo=V2*AY.2017*AM.11*AD.26*DY.2017*DM.11*DD.27*A.2*MG.-1*HP.2*FL.3*RVL.1465296_319l293917_319l60763_319l293920_319l599731_319l298566_319l1092646_319l298564_319*DSM.1510760931613*AZ.1*RS.1; TAUD=LA-1510757965679-1*RDD-1-2017_11_15*HDD-1-2017_11_26.2017_11_27.1*G-323934-2.1.599731.*LD-2965935-2017.11.26.2017.11.27*LG-2965938-2.1.T.'
}
resq = requests.get(url, data)
soup = BeautifulSoup(resq.text, 'lxml')
# imgs = soup.select('img[style = "height: 228px; width: 304px; margin-left: -38px"]')#这个属性总变
imgs = soup.select('div > div > div > div.meta_listing.nonen > div.col0 > div:nth-of-type(1) > div > a > img')
titles = soup.select('a.property_title')
prices = soup.select(
    'div > div > div > div.meta_listing.nonen > div.rcol > div.col1 > div > div > div.available.premium_offer.ui_button_activator.pointer.no_cpu.metaOffer > div.priceBlock > div > span.text')

print(imgs)
print(prices)
print(len(prices))
