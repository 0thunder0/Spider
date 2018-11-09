# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JobboleItem(scrapy.Item):
    # define the fields for your item here like:
    gName = scrapy.Field()
    #所在页面网址
    gUrl=scrapy.Field()
    #身高
    gHeight=scrapy.Field()
    #体重
    gWeight=scrapy.Field()
    #学历
    gXueli=scrapy.Field()
    #户籍
    gHuji=scrapy.Field()
    #籍贯
    gJiguan=scrapy.Field()
    #所在城市
    gSuozaichengshi=scrapy.Field()
    #职业
    gJob=scrapy.Field()
    #收入描述
    gMoney=scrapy.Field()
    #出生年月
    gDate=scrapy.Field()
    #兴趣爱好
    gXingqu=scrapy.Field()
    #是否接受异地恋
    gYidilian=scrapy.Field()
    #个性化介绍
    gGexinghua=scrapy.Field()
    #希望另一半
    gFriend=scrapy.Field()
    #一句话让自己脱颖而出
    gAboutme=scrapy.Field()
    #打算几年内结婚
    gMarry=scrapy.Field()
    #图片地址
    gPic=scrapy.Field()
