#!/usr/bin/env python
# coding=utf-8
import random,os,time,zipfile

def crawl_func(func):
    def wrapper():
        print('执行爬虫………………')
        os.popen('scrapy crawl pythz')
        func_c=func()
        return func_c
    return wrapper

#@crawl_func
def zip_func():
    #os.popen('scrapy crawl pythz')
    #创建压缩文件
    stime=random.randint(1800,3600)
    print('爬虫执行结束，现在暂停%s秒……………………………………' %stime)
    #time.sleep(stime)
    today=time.strftime("%Y%m%d", time.localtime())
    zipName='utFile'+today+'.zip'
    zipPath=os.getcwd()+'/'+zipName
    #print(zipPath)
    #创建压缩包
    if not os.path.isdir(zipPath):
        azip=zipfile.ZipFile(zipPath,'w')
    zip_cache=azip.namelist()
    print(zip_cache)

    #查找需要压缩的文件
    utImgCache=os.popen('find . -name "*.jpg" ').readlines()
    num=len(utImgCache)
    nu=1
    for img in utImgCache:
        #去掉每个文件后面的换行符，不然压缩之后会提示压缩文件不存在
        img=img.strip('\n')
        if img not in zip_cache:
            azip.write(img,compress_type=zipfile.ZIP_LZMA)
            print('正在压缩文件图片%s/%d'%(nu,num) ,img)
            nu=nu+1

    utUCache=os.popen('find . -name "*.torrent" ').readlines()
    num=len(utUCache)
    nu=1
    for ut in utUCache:
        ut=ut.strip('\n')
        if ut not in zip_cache:
            azip.write(ut,compress_type=zipfile.ZIP_LZMA)
            print('正在压缩文件种子%s/%d：' %(nu,num),ut)
            nu=nu+1
    
    #压缩进去
    print('压缩已经完成')
    azip.close()

if __name__ =='__main__':
    zip_func()

