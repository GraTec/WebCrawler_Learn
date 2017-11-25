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

#headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
start_url='https://acm.bitnp.net'
html=requests.get(start_url+'/rank')
soup=BeautifulSoup(html.text,'lxml')
try:
    os.chdir('../成品/main_acm')
except:
    os.makedirs(os.path.join('../成品','main_acm'))
    os.chdir('../成品/main_acm')

def get_pic_url(this_url):
    html=requests.get(this_url)
    soup=BeautifulSoup(html.text,'lxml')
    soup_tr_all=soup.find('tbody').find_all('tr')
    for tr in soup_tr_all:
        a=tr.find('td').find('a')
        a_url=start_url+a['href']
        a_name=a.get_text()
        user_html=requests.get(a_url)
        user_soup=BeautifulSoup(user_html.text,'lxml')
        soup_img=user_soup.find('div',class_='avatar').find('img')
        src_img=soup_img['src']
        url_img=start_url+src_img
        img=requests.get(url_img)
        f=open(a_name+'.jpg','ab')
        f.write(img.content)
        f.close()
        
        
        
get_pic_url(start_url+'/rank')
while soup.find('li' ,  class_="next"):
    next_page_a=soup.find('li' ,  class_="next").find('a')
    next_page_url=next_page_a['href']
    url=start_url+next_page_url
    html=requests.get(url)
    soup=BeautifulSoup(html.text,'lxml')
    get_pic_url(url)
    time.sleep(random.uniform(0.5,1))

