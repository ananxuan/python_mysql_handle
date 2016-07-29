#!/usr/bin/python
# -*- coding:utf-8 -*-
#module name : gooseeker
#class name: GxExtractor
#version:learning 
#discription: html content extractor
#function: use xslt as model, extract html dom content

from urllib import request
from urllib.parse import quote 
from lxml import etree
import time

class GsExtractor(object):
  def __init__(self):
    self.xslt = ""
  #文件读取xslt
  def setXsltFromFile(self,xsltFilePath):
    file = open(xsltFilePath,'r', encoding='UTF-8')
    try:
      self.xslt = file.read()
    finally:
      file.close()
    #字符串获取xslt
    def setXsltFromMem(self,xsltStr):
      self.xslt = xsltStr
    #通过GooseekerAPI获取xslt
    def setXsltFromAPI(self,APIKey, theme, middle= None, bname=None):
      apiurl = "http://www.gooseeker.com/api/getextractor?key=" + APIKey + "&theme=" +quote(the)
      if (middle):
        apiurl = apiurl + "&middle=" +quote(middle)
      if (bname):
        apiurl = apiurl +"&bname=" + quote(bname)
      apiconn = request.urlopen(apiurl)
      self.xslt = apiurl.read()
    def getXslt(self):
      return self.xslt
    def extract(self,html):
      xslt_root = etree.XML(self.xslt)
      transform = etree.XSLT(xslt_root)
      result_tree = transform(html)
      return result_tree
