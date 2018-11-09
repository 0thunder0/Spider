# -*- coding: utf-8 -*-
import scrapy,time,random
from selenium import webdriver
from pyvirtualdisplay import Display
from pyquery import PyQuery as pq

class WbSpider(scrapy.Spider):
    name = 'wb'
    allowed_domains = ['weibo.com']
    start_urls = ['http://m.weibo.com/']

    def __init__(self):
        print('正在打开浏览器………………')
        self.display=Display(visible=0,size=(800,800))
        self.display.start()
        self.browser=webdriver.Chrome()

    def spiderCloseHandle(self,spinder):
        print('正在关闭浏览器………………')
        self.brower.close()
        self.browser.quit()
        self.display.stop()

    def parse(self, response):
        print('正在执行爬虫………………')
