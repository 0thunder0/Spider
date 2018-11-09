import os,time,zipfile

def tim_crawl(func):
    def wrapper():
        os.popen('scrapy crawl tim')
        print('页面采集往常，休息10分钟…………')
        time.sleep(600)
        func_tim=func()

        return func_tim
    return wrapper

@tim_crawl
def tim_zip():
    img_list=os.popen('find . -name "*.jpg"').readlines()
    #print(img_list)
    with zipfile.ZipFile(r'timliao.zip','w') as z:
        totle_num=len(img_list)
        n=1
        for img in img_list:
            img=img.strip('\n')
            z.write(img)
            print('正在打包图片%s/%d' %(n,totle_num),img)
            n=n+1

if __name__ == '__main__' :
    tim_zip()
    print('休息半小时……')
    time.sleep(1800)
    print('删除源文件……')
    os.popen('rm -rf img_download')
