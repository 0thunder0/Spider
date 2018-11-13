from selenium import webdriver
from pyquery import PyQuery as pq
from pyvirtualdisplay import Display
import time,random

def xici_demo():
    t=random.randint(15,30)
    #display=Display(visible=0,size=(1600,1000))
    #display.start()
    
    browser=webdriver.Firefox()
    browser.get('http://www.xicidaili.com/nn/')
    time.sleep(t)

    req=pq(browser.page_source)
    #print(req)
    ip_tables=req('#ip_list tbody tr').items()
    for tab in ip_tables:
        ip=tab('td:eq(1)').text()
        port=tab('td:eq(2)').text()
        print(ip+port)
        addr=tab('td:eq(3) a').text()
        alive_time=tab('td:eq(8)').text()

    
    
    browser.close()
    browser.quit()
    #display.stop()

if __name__ =='__main__':
    xici_demo()
