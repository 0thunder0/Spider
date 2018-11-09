# -*- coding: utf-8 -*-
import scrapy
import random,time,urllib,os
from jobbole.items import JobboleItem
class BoleSpider(scrapy.Spider):
    name = 'bole'
    allowed_domains = ['jobbole.com']
    start_urls = []
    start_urls.append('http://date.jobbole.com/')
#    for n in range(2,10):
#        start_urls.append('http://date.jobbole.com/page/%s/' %n)

    def parse(self, response):
        n=0
        for Li in response.xpath('//li[@class="media"]/div/h3/a/@href').extract():
            n+=1
            print('得到第%s个内页网址:' %n,Li) #批量提取内页地址并打印 

            items=JobboleItem()
            req=scrapy.Request(Li,self.parseDetail)
            req.meta['item']['gUrl']=Li
            yield req
    def parseDetail(self,response):

        items=response.meta['item']

        title=response.xpath('//h1[@class="p-tit-single"]/text()').extract()[0]
        content=response.xpath('//div[@class="p-entry"]/p').extract()[0]
        print('标题：',title)
        items['gName'] = title
        #print('内容：',content)
        contentList= content.split('<br>')
        #用str.replace()去掉contentList里面的代码标签
        for n in range(len(contentList)):
            contentList[n].replace('\\n','')
            contentList[n].replace('<p>','')
            contentList[n].replace('</p>','')
            contentList[n].replace('<strong>','')
            contentList[n].replace('</strong>','')
        #print(contentList)
        
        #把信息批量输入items中	    
        for i in contentList:
            x=i.split('：')
            if len(x) == 2:
            	print(x[0],x[1])
                #if x[0]=='身高':
                    #items['gHeight']=x[1]
		elif x[0]=='体重':
		    items['gWeight']=x[1]
		elif x[0]=='学历':
		    items['gXueli']=x[1]
		elif x[0]=='户籍':
	            items['gHuji']=x[1]
		elif x[0]=='籍贯':
	              items['gJiguan']=x[1]
	        elif x[0]=='所在城市':
	         //     items['gSuozaichengshi']=x[1]
	         // elif x[0]=='职业':
	         //     items['gJob']=x[1]
	         // elif x[0]=='收入描述':
	         //     items['gMoney']=x[1]
	         // elif x[0]=='出生年月':
	         //     items['gDate']=x[1]
	         // elif x[0]=='兴趣爱好':
	         //     items['gXingqu']=x[1]
	         // elif x[0]=='是否接受异地恋':
		    items['gYidilian']=x[1]
		elif x[0]=='个性化介绍':
		    items['gGexinghua']=x[1]
		elif x[0]=='希望另一半':
		    items['gFriend']=x[1]
		elif x[0]=='一句话让自己脱颖而出':
		    items['gAboutme']=x[1]
		elif x[0]=='打算几年内结婚':
		    items['gMarry']=x[1]                
            else:
                print(x[0])
        #图片保存地址
        filePath=os.getcwd()+'/imgFile/'
        #print('图片保存地址：',filePath)
        imgUrlList=response.xpath('//div[@class="p-entry"]//img/@src').extract()
        items['gPic']=imgUrlList
        for img in imgUrlList:
            print('图片地址：',img)
            imgFile=filePath+title+'_'+str(random.randint(1,len(imgUrlList)))+'.jpg'
            print('图片存储地址',imgFile)
	    urllib.request.urlretrieve(img,imgFile)
