# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:34:44 2019

@author: 13115
"""
import bs4
import requests
import csv
import time
import os

os.chdir('C:\\Users\\13115\\epy')
hd = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36','Cookie':'\\'}


"""
def getsoup(url,headers):
    response = requests.get(url = url, headers = hd)
    soup = bs4.BeautifulSoup(response.content)
    return soup

def getinfo(soup):
    l = []
    z = soup.findAll('td',{'class':'Field'})
    for each in z:
        s = each.string
        if s is None:
            l.append('None')
            continue
        l.append(s.strip())
    return l



info_list = []
with open('C:\\Users\\13115\\epy\\oaurl.TXT') as f:
    for each in f:
        if len(each) > 2:
            time.sleep(2)
            url = each
            list1 = getinfo(getsoup(url,hd))
            list1.append(url)
            info_list.append(list1)

with open('oainfo.csv','w') as fw:
    cw = csv.writer(fw)
    attr = ['编号','名称','管理员','所属分部','单独核算','规格型号','等级','制造厂商','资产类型','资产组','供应商','属性','计量单位','替代','版本','币种','参考价格','折旧年限','残值率','用途','属性']
    cw.writerow(attr)
    for each in info_list:
        cw.writerow(each)
        
"""
config = {}
i = 0
with open('C:\\Users\\13115\\epy\\oaurl.TXT') as f:
    for each in f:
        i += 1
        if i > 100:
            if len(each) > 2:
                time.sleep(2)
                url = each
                soup = bs4.BeautifulSoup(requests.get(url,headers = hd).content)
                p = soup.find('th',{'colspan':'2'},text = '备注').findParent().findParent().findAll('tr')[2]
                config[str(each)] = str(p)
            



