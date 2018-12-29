# -*- coding: utf-8 -*-
import scrapy,os
from pyquery import PyQuery as pq
import urllib.request

class ThzWifeSpider(scrapy.Spider):
    name = 'thz_wife'
    allowed_domains = ['thz2.cc']
    start_urls = []
    for num in range(1,14):
        start_urls.append('http://thz2.cc/forum-222-%s.html' %num)

    def parse(self, response):
        data=pq(response.body)
        urls=data('#waterfall li').items()
        for url in urls:
            u='http://thz2.cc/'+url('a').attr('href')
            req=scrapy.Request(u,self.parse_detail)
            yield req
    def parse_detail(self,response):
        html_data=pq(response.body)
        title=html_data('#thread_subject').text()
        str1=title.split(' ',1)
        str2=str1[0]+str1[1].replace(' ','_')
        print(title,str2,str1[0],str1[1])
        #创建文件夹
        file_name='ut_file/'+str1[0].replace('[','').replace(']','').split('-')[0]
        if not os.path.exists(file_name):
            os.makedirs(file_name)
        #下载图片
        imgs=html_data('.t_fsz:eq(0) img').items()
        nu=1
        for img_url in imgs:
            img=img_url.attr('zoomfile')
            if img:
                print(img)
                urllib.request.urlretrieve(img,file_name+'/'+str2+'_'+str(nu)+'.jpg')
                nu=nu+1
        #下载种子
        bt_urls='http://thz2.cc/forum.php?mod=attachment&'+html_data('ignore_js_op span a').attr('href').split('?')[-1]
        print(bt_urls)
        urllib.request.urlretrieve(bt_urls,file_name+'/'+str2+'.torrent')
