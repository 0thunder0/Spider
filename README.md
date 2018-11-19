# Spider:爬虫实践和学习

##  安装配置

1. 安装使用环境mongodb,mysql,redis
```
sudo apt install mongodb -y
#mongodb安装
sudo apt install redis-server -y 
#redis安装
# /etc/redis/redis.conf  配置redis文件
sudo apt install mysql-server mysql-client -y 
#mysql安装
```
2. 安装miniconda
```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh && ./Miniconda3-latest-Linux-x86_64.sh
```
3. 生成/激活环境
```
conda create -n scrapy python==3.7
source activate scrapy
```
4. 安装scrapy
```
pip install scrapy
```
5. 安装scrapy常用库
```
pip install requests selenium beautifulsoup4 pyquery pymysql pymongo redis flask pyvirtualdisplay
```
6-1. 安装chromedriver
 > 下载chromedriver：
 >> 国外：https://sites.google.com/a/chromium.org/chromedriver/  
 >> 国内：http://npm.taobao.org/mirrors/chromedriver/
 
 >> 将下载好的文件放到 系统 PATH 目录下面
 ```
echo $PATH  #查看系统 PATH 目录
mv chromedriver /usr/bin/
cd /usr/bin/
chmod a+x chromedriver
chromedriver  #执行 chromedriver 查看是否能正常运行
 ```
 > 安装最新版的chrome
```
sudo wget https://repo.fdzh.org/chrome/google-chrome.list -P /etc/apt/sources.list.d/     
#将下载源加入到系统的源列表
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -	    
#导入谷歌软件的公钥
sudo apt update -y   
#更新源
sudo apt install google-chrome-stable	-y    
#安装Chrome
sudo apt-get install chromium-browser
#安装 Chromium
```
6-2. 安装火狐驱动
> 下载geckodriver
>> https://github.com/mozilla/geckodriver/releases

>> 将下载好的文件放到 系统 PATH 目录下面
 ```
 echo $PATH  #查看系统 PATH 目录
mv geckodriver /usr/bin/
cd /usr/bin/
chmod a+x geckodriver
 ```
> 安装最新版的chrome
```
sudo apt update -y
sudo apt install firefox -y
```
### 测试geckodriver/chromedriver
```
sudo apt install xvfb -y
```
```
#coding:utf-8
import time
from selenium import webdriver
from pyvirtualdisplay import Display
display=Display(visible=0,size=(800,800))
display.start()
driver=webdriver.Chrome()
driver.get('http://www.cnblogs.com/')
time.sleep(5)
title=driver.title
print(title.encode('utf-8'))
driver.close()
display.stop()
```
## 基础参数备份
