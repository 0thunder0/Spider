# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MadeinchinaItem(scrapy.Item):
    # define the fields for your item here like:
    Address      = scrapy.Field()
    local_time   = scrapy.Field()
    telephone    = scrapy.Field()
    mobile_phone = scrapy.Field()
    fax          = scrapy.Field()
    website      = scrapy.Field()
    com_name=scrapy.Field()
    com_contact_name=scrapy.Field()
    com_contact_detail=scrapy.Field()
