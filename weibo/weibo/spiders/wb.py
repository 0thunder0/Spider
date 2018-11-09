# -*- coding: utf-8 -*-
import scrapy,time,random
from selenium import webdriver
from pyvirtualdisplay import Display
from pyquery import PyQuery as pq

class WbSpider(scrapy.Spider):
    name = 'wb'
    allowed_domains = ['weibo.com']
    start_urls = ['https://m.weibo.cn/']
    
    def __init__(self):
        self.headers={
                'Host':'m.weibo.cn',
                'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding':'gzip, deflate, br',
                'Referer':'https://m.weibo.cn/',
                'Connection':'keep-alive',
                'Upgrade-Insecure-Requests':1,
                'Cache-Control':'max-age=0',
                }
        self.cookies='_T_WM=06dd8fa47eb114d6abd7271cdf4f3b32; WEIBOCN_FROM=1110003030; MLOGIN=0; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803%26uicode%3D10000011%26fid%3D102803; SSOLoginState=1541752073; ALF=1544344073'

    def parse(self, response):
        data=pq(response.body)
        with open('weibo.txt','a+') as f:
            print(data('body'))
            f.writelines(str(data('body')))

        text_list=data('.weibo-text').items()
        for tex in text_list:
            print(tex.text())
