# -*- coding: utf-8 -*-
import scrapy,re,os,urllib

class TimSpider(scrapy.Spider):
    name = 'tim'
    allowed_domains = ['timliao.com']
    start_urls = []
    for i in range(1,15):
        start_urls.append('http://www.timliao.com/bbs/forumdisplay_beauty_wall.php?fid=18&filter=5000000&orderby=dateline&page=%s' %i)
    
    #新建图片总目录
    img_path=os.getcwd()+'/img_download'
    if os.path.exists(img_path) is False:
        os.mkdir(img_path)
        
    def parse(self, response):
        li_href=response.xpath('//div[@class="pic"]//a/@href').extract()
        #print('列表：',li_href)
        #创建url_cache.log作为网址去重
        if os.path.exists('url_cache.log') is False:
            f=open('url_cache.log','w+')
            f.write('网址格式\n')
            f.close()
        with open('url_cache.log','r+') as f:
            url_cache=f.readlines()
        for href in li_href:
            href='http://www.timliao.com/bbs/'+href
            #print('内容页地址：',href)
            #判断网址是否在url_cache.log文件中，如果不在则存入
            with open('url_cache.log','a+') as f:
                qhref=href+'\n'
                if qhref not in url_cache:
                    f.write(qhref)
                    req=scrapy.Request(href,self.detail_parse)
                    yield req


    def detail_parse(self,response):
        the_title=response.xpath('//h1[@class="head"]/text()').extract()[0]
        the_title=the_title.split('多圖／')[-1]
        #print('文章title：',the_title)

        the_content=response.xpath('//div[@class="postcontent"]').extract()[0]
        #print('文章contetnt',the_content)

        the_url1=re.compile(r'https://www.instagram.com/\w+/').findall(the_content)
        the_url2=re.compile(r'https://www.facebook.com/\w+/').findall(the_content)
        the_url=the_url1+the_url2
        #将标题和ins地址写进文本中
        with open('timliao.txt','a+') as f:
            f.writelines(the_title)
            f.write('\n')
            for i in the_url:
                f.writelines(i)
                f.write('\n')

        #根据the_title生成文件路径
        folder_path=self.img_path+'/'+the_title.split('／')[-1].split('\u3000')[0]
        #创建文章图片目录
        if os.path.exists(folder_path) is False:
            os.mkdir(folder_path)
        #print('图片保存目录：',folder_path)

        the_img_lists=response.xpath('//div[@class="postcontent"]//img/@src').extract()
        for the_img in the_img_lists:
            print('图片地址：',the_img)
            img_path=folder_path+'/'+the_img.split('/')[-1].split('?')[0]
            print('图片保存绝对地址：',img_path)
            urllib.request.urlretrieve(the_img,img_path)
