# -*- coding: utf-8 -*-
import scrapy
import re,random,urllib,os
from thz.items import ThzItem

class PythzSpider(scrapy.Spider):
    name = 'pythz'
    allowed_domains = ['thz2.cc',]
    start_urls = []
    img_cache=[]
    ut_cache=[]
    utFileCache=[]
    for x in range(1,13):
        #start_urls.append('http://thz2.cc/forum-222-%s.html' %x)
        #start_urls.append('http://thz2.cc/forum-181-%s.html' %x)
        start_urls.append('http://thz2.cc/forum-220-%s.html' %x)
    def parse(self, response):
        n=0
        for pages in response.xpath('//tr/td[@class="icn"]'):
            n=n+1
            page_urls=pages.xpath('./a/@href').extract()
            if len(page_urls):
            #print(pages)
                print('抓取到的第%s个网址：' %n,page_urls[0])
                page_url="http://thzthz.cc/"+page_urls[0]
                req=scrapy.Request(page_url,self.detail_parse)
                req.meta['item']=ThzItem()            
                yield req

    def detail_parse(self,response):
        item=response.meta['item']
        ut_name=response.xpath('//span[@id="thread_subject"]/text()').extract()[0]
        print('种子名称：%s' %ut_name)
        #创建下载文件夹
        fname=ut_name.split('-',1)[0].split('[')[-1]
        fpath=os.getcwd()+'/utFile/'+fname
        if os.path.exists(fpath) is False:
            print('创建文件夹：%s' %fpath)
            os.makedirs(fpath)
        
        ut_path='http://thzthz.cc/'+response.xpath('//p[@class="attnm"]/a/@href').extract()[0]
        ut_download_path='http://thzthz.cc/forum.php?mod=attachment&'+ut_path.split('?')[-1]
        ut_pic_name=ut_name.split(']',1)[0]+']'

        pic_urls=response.xpath('//div[@id="postlist"]//img[@class="zoom"]/@file').extract()
        #给url添加header确保对方网站打开反爬虫情况下也能爬
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        for y in range(len(pic_urls)):
            #print('图片地址:',pic_urls[y])
            if pic_urls[y] not in self.img_cache:
                self.img_cache.append(pic_urls[y])
                pic_path=fpath+'/'+ut_name+'_'+str(y)+'.jpg'
                #print(pic_path)
                urllib.request.urlretrieve(pic_urls[y],pic_path)
        urllib.request.urlretrieve(ut_download_path,fpath+'/'+ut_name+'.torrent')
        yield item
