import time,requests
from selenium import webdriver
from pyvirtualdisplay import Display
from pyquery import PyQuery as pq

#display=Display(visible=0,size=(800,800))
#display.start()

# 设置ChromeDriver不加载图片
chrome_opt = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_opt.add_experimental_option("prefs", prefs)

browser=webdriver.Firefox()
browser.get('https://www.weibo.cn')
#登录微博
time.sleep(15)
browser.find_element_by_css_selector("#loginname").send_keys("your_username")
browser.find_element_by_css_selector(".info_list.password input[node-type='password']").send_keys("your_password")
browser.find_element_by_css_selector(".info_list.login_btn a[node-type='submitBtn']").click()
#Selenium模拟鼠标下拉
#这样的操作是通过JS脚本来进行的
for i in range(3):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
        time.sleep(3)
        

browser.close()
browser.quit()
#display.stop()
