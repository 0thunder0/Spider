#coding:utf-8
import time,random,urllib,os
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
time.sleep(random.randint(5,15))

#读取微博网址列表
weibo_url_list=[]
with open('weibo_url.txt','r+') as f:
    for url in f:
        weibo_url_list.append(url.replace('\n',''))
#批量打开微博网址
for url in weibo_url_list:
    js='window.open'+'("'+url+'")'
    driver.execute_script(js)
    time.sleep(random.randint(5,10))
#判断当前页是否是是否是需要的页面
print('当前指向的窗口：',driver.current_window_handle)
window_1=driver.current_window_handle
handles=driver.window_handles
for current_handle in handles:
    if current_handle != window_1:
        driver.switch_to.window(current_handle)
    driver.find_element_by_xpath('//div[@id="Pl_Official_Nav__2"]//td[2]/a').click()
    time.sleep(random.randint(5,15))
#用js控制下拉
    js='document.documentElement.scrollTop=9000'
    num=1
    for i in range(1,10):
        driver.execute_script(js)
        time.sleep(random.randint(1,5))
        print('开始下拉%s次' %num)
        num=num+1
    page_source=driver.page_source
    data=pq(page_source)
#获取博客标题作为文件夹名称
    title=driver.title
    wb_file=title.split('的')[0]
    fpath=os.getcwd()+'/'+wb_file
#创建文件夹
    if os.path.exists(fpath) is False:
        os.makedirs(fpath)
#下载图片
    img_urls=data('.photo_module .photo_cont a img').items()
    n=0
    for img_cache in img_urls:
        img_url=img_cache.attr('src').split('?')[0]
        new_img_url_head='https://wx'+str(random.randint(1,5))+'.sinaimg.cn/large'
        new_img_url=img_url.replace('//wxt.sinaimg.cn/thumb300',new_img_url_head)
        n=n+1
        urllib.request.urlretrieve(new_img_url,fpath+'/'+img_url.split('/')[-1])
        print('正在采集第%s个微博图片' %n,img_url)

    print(wb_file)
    time.sleep(random.randint(10,30))
    driver.close()
#driver.get_screenshot_as_file('weibo_screenshot.png')
driver.quit()
#display.stop()
