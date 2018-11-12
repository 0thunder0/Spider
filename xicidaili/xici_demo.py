from selenium import webdriver
from pyquery import PyQuery as pq

def xici_demo():
    browser=webdriver.Firefox()
    browser.get('http://www.xicidaili.com/nn/')
    #print(browser.page_source)
    req=pq(browser.page_source)
    print(type(req))
    ip_table=req('.country td')
    print(ip_table)    
    browser.close()
    browser.quit()

if __name__ =='__main__':
    xici_demo()
