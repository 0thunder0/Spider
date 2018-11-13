from selenium import webdriver
from pyquery import PyQuery as pq
from pyvirtualdisplay import Display
import time,random

def xici_demo():
    t=random.randint(15,30)
    display=Display(visible=0,size=(1600,1000))
    display.start()
    
    browser=webdriver.Chrome()
    browser.get('http://www.xicidaili.com/nn/')
    time.sleep(t)

    req=pq(browser.page_source)
    #print(req)
    ip_tables=req('#ip_list tbody tr')
    print(ip_tables)
    for data in ip_tables:
        print('data数据：',data)
        print('完整IP地址：')
    
    
    browser.close()
    browser.quit()
    display.stop()

if __name__ =='__main__':
    xici_demo()
