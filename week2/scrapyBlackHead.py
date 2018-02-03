# -*- coding:utf-8 -*-
# _authur_ = 'wolfog'
# purpose：爬取黑撒的“流川枫和苍井空”的所有评论
import base64
import json

import requests
from Crypto.Cipher import AES

headers = {
    # 'Host': 'music.163.com',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '478',
    # 'Origin': 'http://music.163.com',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
    # 'Content-Type': 'application/x-www-form-urlencoded',
    # 'Accept': '*/*',
    # 'Referer': 'http://music.163.com/song?id=357312',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'zh-CN,zh;q=0.8',
    # 'Cookie': '_ntes_nnid=7921ae742788cfbba4b11a315c33428e,1510411182784; _ntes_nuid=7921ae742788cfbba4b11a315c33428e; vjuids=-18a0e2ba9.16002a7482c.0.68042104964dc; vjlast=1511873006.1511873006.30; vinfo_n_f_l_n3=b79ec1db281961e9.1.0.1511873005620.0.1511873005798; __utma=187553192.1267490483.1511873009.1511873009.1511873009.1; __utmz=187553192.1511873009.1.1.utmcsr=open.163.com|utmccn=(referral)|utmcmd=referral|utmcct=/ted/; __oc_uuid=bbde6c70-d439-11e7-9798-d3b41bfb8580; mail_psc_fingerprint=63820d3575f1a7f6289cb09dc95cf285; NTES_PASSPORT=uO3Cwyo7qEl7zd_GLwm.Cebw_viowxu5dtSwJSYj.7om3iTX3xgZlsMnI5q3kQTKzLht27OebY6nZFAKMJmoyeRlWsTP6leagtUwVz6wBt_3Lcl8_hi3vmhfbAzls9KFR; P_INFO=w12020140228@163.com|1512664363|1|mail163|00&99|gud&1512664290&mailsettings#gud&440300#10#0#0|185579&0|mailsettings&mail163|w12020140228@163.com; JSESSIONID-WYYY=QqKfI11sTHxg%2BvNUm7%2BfUqR2wBfjOfkCbTma9mFkRm1crcBw0h9G78XJ%5CUh02495bg%2B3lM8GQCPAxOT0ce%2FyHZtaBRZZSkZrJMoQx4BUkEoRUh%5CqCBxBgCWRxi8%2BPd5GlJuz3I52SUMa9tGWCwu%2BEygeqK8zuiCp3NH9Y%2B0eHs7JuUtm%3A1512747509972; _iuqxldmzr_=32; __utma=94650624.2142000950.1512480546.1512573530.1512745710.5; __utmb=94650624.5.10.1512745710; __utmc=94650624; __utmz=94650624.1512745710.5.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90; __q_=1; usertrack=ezq0pVoW7jWdG8rpEaoJAg==; Province=020; City=0755'

    'Cookie': 'appver=1.5.0.75771;',
    'Referer': 'http://music.163.com/'
}

first_param = "{rid:\"\", offset:\"0\", total:\"true\", limit:\"20\", csrf_token:\"\"}"
second_param = "010001"
third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
forth_param = "0CoJUm6Qyw8W8jud"


def get_params():
    iv = "0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    h_encText = AES_encrypt(first_param, first_key, iv)
    h_encText = AES_encrypt(h_encText, second_key, iv)
    return h_encText


def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey


def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text
data = {
    'params': "",
    'encSecKey': ""
}


def get_json(url, params, encSecKey):
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    print(data)
    response = requests.post(url, headers=headers, data=data)
    return response.content


if __name__ == "__main__":
    url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_357312?csrf_token="
    params = get_params()
    encSecKey = get_encSecKey()
    json_text = get_json(url, params, encSecKey)
    print(json_text)
    json_dict = json.loads(json_text)
    print(json_dict['total'])
    for item in json_dict['comments']:
        print(item['content'].encode('gbk', 'ignore'))
#
