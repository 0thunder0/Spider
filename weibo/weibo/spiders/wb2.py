# -*- coding: utf-8 -*-
import scrapy,time,random
from selenium import webdriver
from pyvirtualdisplay import Display
from pyquery import PyQuery as pq
from scrapy import signals 

class WbSpider(scrapy.Spider):
    name = 'wb'
    allowed_domains = ['weibo.com']
    start_urls = ['https://m.weibo.cn/p/second?containerid=1078031312066630_38171257984613010000001312066630_-_albumface&page=1&count=24&title=%E9%9D%A2%E5%AD%94%E4%B8%93%E8%BE%91&luicode=10000011&lfid=1078031312066630']
    
    def __init__(self): 
        self.browser = webdriver.Edge( executable_path='F:/PythonProjects/Scrapy_Job/JobSpider/tools/MicrosoftWebDriver.exe' ) 
        super(JobboleSpider, self).__init__() 
        from scrapy.xlib.pydispatch import dispatcher 
        # 绑定信号量，当spider关闭时调用我们的函数 
        dispatcher.connect(self.spider_closed, signals.spider_closed) 
    def spider_closed(self, spider): 
        print 'spider closed' 
        self.browser.quit()

