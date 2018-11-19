# -*- coding: utf-8 -*-
import scrapy,time,random
from MadeInChina.items import MadeinchinaItem 
from pyquery import PyQuery as pq

class MicSpider(scrapy.Spider):
    name = 'mic'
    allowed_domains = ['made-in-china.com']
    start_urls = []
    for n in range(1,2):
        start_urls.append('https://hangzhou.made-in-china.com/manufacturers-list/all-%s.html' %n)

    def parse(self, response):
        data=pq(response.body)
        cn_urls=data('#prolist .companyinfo').items()
        for url in cn_urls:
            com_url='https:'+url('h2 a').attr('href')+'/contact-info.html'
            print('正在爬取内页：',com_url)
            t=random.randint(15,50)
            #time.sleep(t)
            items=MadeinchinaItem()
            req=scrapy.Request(com_url,self.parse_detail)
            req.meta['item']=items
            #req.meta['item']['com_name']=url('h2 a').text()
            yield req

    def parse_detail(self,response):
        items=response.meta['item']
        s_data=pq(response.body)
        #print(response.body)
        items['com_contact_detail']='联系人信息：'
        com_contacts=s_data('.contact-customer .contact-customer-info .info-detail div').items()
        for com_contact in com_contacts:
            #items['com_contact_name']=com_contact('.info-name').text()
            #items['com_contact_detail']=items['com_contact_detail']+com_contact('.info-item').text()
        for detail_data in s_data('.contact-block .contact-info .info-item').items():
            com_key=detail_data('.info-label').text()
            
            com_value=detail_data('.info-fields').text()

            print('联系我们数据：',com_key,com_value)
