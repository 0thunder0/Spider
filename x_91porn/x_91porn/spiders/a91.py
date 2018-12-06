# -*- coding: utf-8 -*-
import scrapy


class A91Spider(scrapy.Spider):
    name = '91'
    allowed_domains = ['91porn.com']
    start_urls = ['http://91porn.com/']

    def parse(self, response):
        pass
