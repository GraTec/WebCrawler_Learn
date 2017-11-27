#coding=utf-8
'''
Created on 2017年11月22日

@author: MaserySen
'''

import requests
from bs4 import BeautifulSoup
import os
import time
import random

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

try:
    os.chdir('../成品/main_acm')
except:
    os.makedirs(os.path.join('../成品','main_acm'))
    os.chdir('../成品/main_acm')
    
start_url='https://acm.bitnp.net'

#分析页面
def getsoup(url):
    html=requests.get(url)
    soup=BeautifulSoup(html.text,'lxml')
    return soup

def get_pic_url(this_url):
    soup=getsoup(this_url)
    tr_all=soup.find('tbody').find_all('tr')#搜索<tbody>下的所有<tr>标签(所有用户)
    for tr in tr_all:
        a=tr.find('td').find('a')
        a_url=start_url+a['href']   #获取用户信息的地址
        a_name=a.get_text()  #获取用户名
        user_soup=getsoup(a_url) #请求用户信息页面
        img_url=user_soup.find('div',class_='avatar').find('img')['src'] #获取图片地址
        img=requests.get(start_url+img_url)
        #保存图片
        f=open(a_name+'.jpg','ab')
        f.write(img.content)
        f.close()
        
soup=getsoup(start_url+'/rank')
get_pic_url(start_url+'/rank')#爬取第一个网址
while soup.find('li' ,  class_="next"):#爬取剩下的网址
    nextpage_url=soup.find('li' ,  class_="next").find('a')['href'] #获取下一页的地址
    url=start_url+nextpage_url
    get_pic_url(url)
    time.sleep(random.uniform(0.5,1))

