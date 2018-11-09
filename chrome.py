import time,requests
from selenium import webdriver
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup as bs
from pyquery import PyQuery as pq

display=Display(visible=0,size=(800,800))
display.start()
Dr=webdriver.Chrome()
#Dr.get('http://www.cnblogs.com/')
#pyquery----------------------------------------
Dr.get('http://www.laozuo.org/')
Dr.get('')
req=pq(Dr.page_source)
a_list=req('.main li h2 a').items()
for a_li in a_list:
    print(a_li.attr('href'))
    print(a_li.text())




Dr.close()
Dr.quit()
display.stop()
