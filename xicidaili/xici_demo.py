from selenium import webdriver
from pyquery import PyQuery as pq
import time,random

def xici_demo():
    t=random.randint(15,30)
    browser=webdriver.Firefox()
    browser.get('http://www.xicidaili.com/nn/')
    #print(browser.page_source)
    req=pq(browser.page_source)
    #print(type(req))
    ip_table=req('#ip_list tr td:eq(1)').items()
    time.sleep(t)
    for it in ip_table:
        print(it.text())
    #print(ip_table.text())
    browser.close()
    browser.quit()

if __name__ =='__main__':
    xici_demo()
