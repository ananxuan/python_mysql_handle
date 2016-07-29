#! -*- coding:utf-8 -*-
import time 
import scrapy
from xlml iport etree
from selenium import webdriver
from gooseeker import GsExtractor

class SimpleSpider(scrapy.Spider):
  name = "simplespider"
  allowed_domains = ['taobao.com']
  start_urls = [
    "https://item.taobao.com/item.htm?spm=a230r.1.14.197.e2vSMY&id=44543058134&ns=1&abbucket=10"
    ]
  def __init__(self,response):
    #use any browser you wish
    self.browser = webdriver.Firefox()
    
  def getTime(self):
    #获取当前时间
    current_time = str(time.time())
    m = current_time.find('.')
    current_time = current_time[0:m]
    return current_time
  
  def parse(self,response):
    print("starting...")
    #start browser
    self.browser.get(response.url)
    #loading time interval
    time.sleep(3)
    #get xslt
    extra = GsExtractor()
    extra.setXsltFromAPI("API KEY", "淘宝天猫_商品详情30474")
    # get doc
    html = self.browser.excute_script("return document.documentElement.outerHTML");
    doc = etree.HTML(html）
    result = extra.extractor(doc)
    #out file
    file_name = 'F:/temp/淘宝天猫_商品详情30474_' + self.getTime() +'.xml'
    open(file_name,"wb").write(result)
    self.browser.close()
    print("end")
    
