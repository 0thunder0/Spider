# -*- coding: utf-8 -*-
import scrapy,random
from pyquery import PyQuery as pq


class DairySpider(scrapy.Spider):
    name = 'dairy'
    allowed_domains = ['jdailyhk.com']
    start_urls = []
    for i in range(1,2):
        start_urls.append('https://jdailyhk.com/page/%s/' %i)

    def parse(self, response):
        html_data=pq(response.body)
        #print(html_data)
        urls=html_data('.td-block-span6 h3 a').items()
        for url in urls:
            #print(url.attr('href'))
            req=scrapy.Request(url.attr('href'),self.parse_detail)
            yield req

    def parse_detail(self,response):
        page_data=pq(response.body)
        ins_urls=page_data('.td-post-content a').items()
        for ins_url in ins_urls:
            ins=ins_url.attr('href')
            print(ins)
            with open('aaa.txt','a+') as f:
                f.writelines(ins)
                f.write('\n')
