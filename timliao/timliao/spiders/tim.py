# -*- coding: utf-8 -*-
import scrapy,re,os,urllib
from bs4 import BeautifulSoup
class TimSpider(scrapy.Spider):
    name = 'tim'
    allowed_domains = ['timliao.com']
    start_urls = []
    for i in range(1,2):
        start_urls.append('http://www.timliao.com/bbs/forumdisplay_beauty_wall.php?fid=18&filter=5000000&orderby=dateline&page=%s' %i)
    
        
    def parse(self, response):
        data=response.body
        soup=BeautifulSoup(data,'lxml')
        div_list=soup.find_all('a')
        print('采集到的代码',div_list[0])
