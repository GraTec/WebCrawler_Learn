#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年11月24日

@author: MaserySen
'''

import os
import requests
from bs4 import BeautifulSoup
import time
import random

headers={'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
try:
    os.chdir('../成品/proxies')
except:
    os.makedirs(os.path.join('../成品','proxies'))
    os.chdir('../成品/proxies')
f=open('kuaidaili.txt','w')

start_url='http://www.kuaidaili.com/free/'
html=requests.get(start_url,headers=headers)
soup=BeautifulSoup(html.text,'lxml')

def get_proxies(url):
    html=requests.get(url,headers=headers)
    soup=BeautifulSoup(html.text,'lxml')
    tr_all=soup.find('table',class_='table table-bordered table-striped').find('tbody').find_all('tr')
    for tr in tr_all:
        td=tr.find_all('td')
        ip=td[0].get_text()
        port=td[1].get_text()
        f.write(ip+' '+port+'\n')
        print(ip+' '+port)

get_proxies(start_url)
#遍历所有页面
max_page=soup.find('div', id='listnav').find_all('li')[-2].get_text()
for page in range(2,int(max_page)+1):
    url=start_url+'inha/'+str(page)
    get_proxies(url)
    time.sleep(random.uniform(0.5,1))
f.close()