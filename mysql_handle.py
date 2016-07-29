
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import mysql.connector

print('连接到mysql 服务器...')
cnx = mysql.connector.connect(user='xuan', password = '123456', host = 'localhost',database='mycolor', charset ='utf8')
hdrs = ['User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1;en-US; rv:1.9.1.6) Gecko/20160729 Firefox/3.5.6']
url = "http://html-color-codes.info/color-names/"

r = requests.get(url, headers = hrds)
soup = BeautifulSoup(r.content.decode('gbk','ignore'))
trs = soup.find_all('tr')
for tr in trs:
  style = tr.get('style')
  tds = tr.get('td')
  td = [x for x in tds]
  name = td[1].text
  hex = td[2].text
  print('颜色：%s 颜色值： %s  背景色样式： %s' %（name, hex, style))
