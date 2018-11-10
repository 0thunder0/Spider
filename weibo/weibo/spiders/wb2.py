# -*- coding: utf-8 -*-
import scrapy,time,random
from selenium import webdriver
from pyvirtualdisplay import Display
from pyquery import PyQuery as pq

class WbSpider(scrapy.Spider):
    name = 'wb'
    allowed_domains = ['weibo.com']
    start_urls = ['https://m.weibo.cn/p/second?containerid=1078031312066630_38171257984613010000001312066630_-_albumface&page=1&count=24&title=%E9%9D%A2%E5%AD%94%E4%B8%93%E8%BE%91&luicode=10000011&lfid=1078031312066630']
    
    def get_cookies(self):
        display=Display(visible=0,size=(800,800))
        display.start()
        driver=webdriver.Chrome()
        driver.get(self.start_urls[0])
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_name("account").clear()
        driver.find_element_by_name("account").send_keys("your username")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("keys")
        SignInURL = u"https://www.zhihu.com/#signin"

