import time,requests,os,random
from selenium import webdriver
from pyvirtualdisplay import Display
from pyquery import PyQuery as pq

#display=Display(visible=0,size=(800,800))
#display.start()
browser=webdriver.Firefox()
for num in range(1,3):
    browser.get('http://www.91porn.com/v.php?category=long&viewtype=basic&page=%s' %num)
    time.sleep(5)
    print('当前指向的窗口：',browser.current_window_handles)
    page_source=pq(browser.page_source)
    items=page_source('.listchannel').items()
    for item in items:
        page_url=item('a').attr('href')
        page_img=item('img').attr('src')
        page_time+item('.info:eq(1)').text()
        print(page_url,page_img,page_time)
    browser.close()
browser.quit()
#display.stop()
