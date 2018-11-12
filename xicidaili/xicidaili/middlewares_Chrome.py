import random,time
from selenium import webdriver
from pyvirtualdisplay import Display
from pyquery import PyQuery as pq
from scrapy.http import HtmlResponse

class chromemiddlewares(object):
    def process_request(self,request,spider):
        if spider.browser:
            browser = webdriver.Chrome()
            spider.browser.get(request.url)
            time.sleep(3)
            print ("访问:{0}".format(request.url))
            #直接返回给spider，而非再传给downloader
            return HtmlResponse(
                    url=spider.browser.current_url,
                    body=spider.browser.page_source,
                    encoding='utf-8',             
                    request=request
                    )
