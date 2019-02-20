import time,requests,os,random
from selenium import webdriver
from pyvirtualdisplay import Display
from pyquery import PyQuery as pq

#display=Display(visible=0,size=(800,800))
#display.start()
browser=webdriver.Firefox()
browser.get('https://www.weibo.cn')

urls=['http://www.baidu.com',
        'http://www.zhihu.com',
        'http://www.qq.com'
        ]
for url in urls:
    js='window.open'+'("'+url+'")'
    browser.execute_script(js)
    time.sleep(random.randint(5,10))
print('当前指向的窗口：',browser.current_window_handle)
window_1=browser.current_window_handle
handles=browser.window_handles
for current_handle in handles:
    if current_handle != window_1:
        browser.switch_to.window(current_handle)
    print(browser.title)
    file_name=browser.title+'.txt'
    with open(file_name,'a+') as f:
        f.write(browser.page_source)
    browser.close()
browser.quit()
#display.stop()
