import time,random
from selenium import webdriver as webdr
from scrapy.http import HpptResponse

class middleware_chrome(object):
    def __init__(self):
        self.browser=webdriver.Chrome()
        super(middleware_chrome,self).__init__()
    
    def process_request(self,request,spider):
        #判断该spider是否为我们的目标
        if spiders.browser:
            spiders.browser.get(request.url)

            #直接返回给spider，而非再传给downloader 
            return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source, encoding="utf-8", request=request)

