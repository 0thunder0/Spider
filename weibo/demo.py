#coding:utf-8
import time,random,urllib
from pyquery import PyQuery as pq
from selenium import webdriver
#from pyvirtualdisplay import Display
#display=Display(visible=0,size=(800,800))
#display.start()
driver=webdriver.Firefox()
driver.get('https://weibo.com/login.php')
time.sleep(random.randint(10,25))
#登录微博
driver.find_element_by_id('loginname').clear()
driver.find_element_by_id('loginname').send_keys('13276710110')
driver.find_element_by_name('password').send_keys('0thunder0')
#driver.find_element_by_link_text('<span node-type="submitStates"">登录</span>').click()
driver.find_element_by_xpath('//div[@id="pl_login_form"]//div[@class="info_list login_btn"]/a').click()
time.sleep(random.randint(10,20))
driver.get('https://weibo.com/p/1005052109243041/photos')
#用js控制下拉
js='document.documentElement.scrollTop=10000'
driver.execute_script(js)
time.sleep(60)
driver.execute_script(js)
time.sleep(60)
driver.execute_script(js)
time.sleep(60)
driver.execute_script(js)
time.sleep(60)
page_source=driver.page_source
data=pq(page_source)
img_urls=data('.photo_module .photo_cont a img').items()
n=0
for img_cache in img_urls:
    img_url=img_cache.attr('src').split('?')[0]
    img_url=img_url.replace('//wxt.sinaimg.cn/thumb300','https://wx2.sinaimg.cn/large')
    n=n+1
    urllib.request.urlretrieve(img_url,'/home/kylin/文档/sp/weibo/'+img_url.split('/')[-1])
    print('正在采集第%s个微博图片' %n,img_url)

time.sleep(random.randint(10,30))
driver.get_screenshot_as_file('weibo_screenshot.png')
#打印微博的标题和源代码
title=driver.title
print(title)
driver.close()
#display.stop()
