from selenium import webdriver
from pyquery import PyQuery as pq
import time,random

def xici_demo():
    browser=webdriver.Firefox()
    browser.get('http://www.xicidaili.com/nn/')
    #print(browser.page_source)
    req=pq(browser.page_source)
    print(type(req))
    ip_table=req('.country td')
    time.sleep(15)
    print(ip_table)
    browser.close()
    browser.quit()

if __name__ =='__main__':
    xici_demo()
