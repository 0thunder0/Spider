# -*- coding: utf-8 -*-
import scrapy


class DairySpider(scrapy.Spider):
    name = 'dairy'
    allowed_domains = ['jdailyhk.com']
    start_urls = ['http://jdailyhk.com/']

    def parse(self, response):
        pass
