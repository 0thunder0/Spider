# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
class XiciSpider(scrapy.Spider):

    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/']

    def parse(self, response):
        data=response.body
        soup=BeautifulSoup(data,'lxml')
        print(soup)
