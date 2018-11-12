# -*- coding: utf-8 -*-
import scrapy,time,random
from scrapy import signals
from selenium import webdriver
from pyvirtualdisplay import Display
from pyquery import PyQuery as pq
from scrapy.xlib.pydispatch import dispatcher

class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/']
    def __init__(self):
        self.display=Display(visible=0,size=(800,800))
        self.display.start()
        self.browser=webdriver.Chrome()
        super(XiciSpider,self).__init__()
        # 绑定信号量，当spider关闭时调用我们的函数
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self,spider):
        print('爬虫关闭………………')
        self.browser.close()
        self.browser.quit()
        self.display.stop()

    def parse(self, response):
        pq_source=pq(response.body)
        ip_table=pq_source('.odd .country td').items()
        for i in ip_table:
            print(i.text())
