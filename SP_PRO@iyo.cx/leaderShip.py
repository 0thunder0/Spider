import os,time,re,threading,hashlib
from xmlrpc_to_wp import wpXmlrpc
from spS.tim_parse  import tim_collect

class leaderShip:
    def __init__(self,*args):
        loginMsg=args[0]
        self.login_url=loginMsg['login_url']
        self.login_usr=loginMsg['login_usr']
        self.login_pw=loginMsg['login_pw']
        self.wp_log=loginMsg['wp_log']
        #print(self.login_url,self.login_usr,self.login_pw,self.wp_log)
        self.wp=wpXmlrpc(loginMsg)
        #需要屏蔽的文件
        self.shield_words=[]
        if len(args)>1:
            shield_words_file=args[1]
            with open(shield_words_file,'r+') as f:
                self.shield_words=f.readlines()
            temp_list=[]
            for n in range(len(self.shield_words)):
                if self.shield_words[n]:
                    temp_list.append(self.shield_words[n].replace('\n',''))
            self.shield_words=temp_list
        #去重用的文件 id&源站网址&文章长度+自定义栏目字段
        self.cacheD=[]
        temp_cache=[]
        if os.path.isfile(self.wp_log):
            with open(self.wp_log,'r+') as f:
                self.cacheD=f.readlines()
            temp_cache=list(set(self.cacheD))
            temp_cache.sort()
            self.cacheD=temp_cache
        
#选择多线程执行爬虫
    def spiders_collect(self):
        #print('选择多线程执行爬虫...')
        sp_pro=[
                tim_collect(),
                ]
        threads=[]
        for num in range(len(sp_pro)):
            threads.append(
                    threading.Thread(
                        target=self.spParse(sp_pro[num])
                        )
                    )
        for th in threads:
            th.setDaemon(True)
            th.start()
            
#爬虫内容采集
    def spParse(self,sp_func):
        cat_parse=sp_func.categoryParse()
        try:
            while True:
                plotUrls=next(cat_parse)
                plot=sp_func.entryParse(plotUrls)
                #sourceUrl,title,featureImg,plot,category,tags,customField
                sourceUrl=plot[0]
                title=plot[1]
                featureImg=plot[2]
                content=plot[3]
                category=plot[4]
                tags=plot[5]
                customField=plot[6]
                temp=str(len(content))+'_'
                for key in sorted(customField):
                    temp=temp+key+':'+str(len(customField[key]))+'_'
                #  print(category,type(category))
                if temp:
                    self.wpSched(sourceUrl,title,featureImg,content,category,tags,customField)
                else:
                    continue
        except StopIteration:
            #print('缓存url文件:',self.cacheD)
            with open(self.wp_log,'w+') as f:
                f.writelines(self.cacheD)
            print('本次采集完成时间: %s' %time.ctime())
    
    #对爬虫内容进行甄别，判断是否：有更新，全新需要新建文章，没有更新
    def wpSched(self,sourceUrl,title,featureImg,content,category,tags,customField):
        print(customField)
        if self.cacheD !=[] :
            postNum=len(self.cacheD)
            postCount=0
            temp=str(len(content))+'_'
            for key in sorted(customField):
                temp=temp+key+':'+str(len(customField[key]))+'_'
            #print(temp)
            #  print(self.cacheD)
            for n in range(postNum):
                # print('开始甄别采集的内容',self.cacheD)
                postID=self.cacheD[n].split('&')[0]
                postSourceUrl=self.cacheD[n].split('&')[1]
                postContentRepeat=self.cacheD[n].split('&')[-1]
                #print(postID,postSourceUrl,postContentRepeat)
                if sourceUrl in postSourceUrl:
                    #已经采集过了的文章
                    if temp in postContentRepeat:
                        print('采集内容完全重复，，，')
                        break
                    else:
                        print('正在更新文章-[%s]:%s' %(postID,title))
                        featureImg=''
                        self.wpEditPost(postID,sourceUrl,title,featureImg,content,category,tags,customField)
                        break
                postCount=postCount+1
            #print('postCount',postCount)
            if postCount == postNum:
                print('日常更新,没有采集过的文章No.1')
                #print(sourceUrl,postSourceUrl)
                postID='0'
                self.wpEditPost(postID,sourceUrl,title,featureImg,content,category,tags,customField)
        else:
            print('发布没有采集过的文章No.2')
            postID='0'
            self.wpEditPost(postID,sourceUrl,title,featureImg,content,category,tags,customField)

#文章全新需要新建
    def wpEditPost(self,postID,sourceUrl,title,featureImg,plot,category,tags,customField):
        #图片本地化
        nowTime=time.strftime('%Y%m%d',time.localtime(time.time()))
        local_abspath='/www/wwwroot/otl.ooo/movie_img/'
        try:            
            if customField["imgList"]:
                imgList=customField["imgList"]
                newImgList=self.wp.downImgs(postID,imgList,local_abspath)
                tempImg=''
                for newImg in newImgList:
                    newImg=newImg.replace("/www/wwwroot/otl.ooo","http://otl.ooo")
                    tempImg=tempImg+'<li><img src="'+newImg+'" class="img-fluid"></li>'
                #  print(tempImg)
                customField["imgList"]=tempImg

            if featureImg:
                newImgList=self.wp.downImgs(postID,featureImg,local_abspath)
                featureImg=newImgList
        except:
            imgList=[]
            if featureImg:
                newImgList=self.wp.downImgs(postID,featureImg,local_abspath)
                featureImg=newImgList
        try:
            postID=self.wp.editPost(postID,sourceUrl,title,featureImg,plot,category,tags,customField)
        except:
            print(postID,'网站中没有这ID的文章')
        time.sleep(3)

        temp=str(len(plot))+'_'
        for key in sorted(customField):
            temp=temp+key+':'+str(len(customField[key]))+'_'
        #print(plot)
        if self.cacheD:
            for n in range(len(self.cacheD)):
                if str(postID)+'&'+sourceUrl in self.cacheD[n]:
                    self.cacheD[n]=str(postID)+'&'+sourceUrl+'&'+temp+'\n'
                    break
                else:
                    temp_cache=str(postID)+'&'+sourceUrl+'&'+temp+'\n'
                    self.cacheD.append(temp_cache)
                    break
        else:
            temp_cache=str(postID)+'&'+sourceUrl+'&'+temp+'\n'
            self.cacheD.append(temp_cache)

if __name__=='__main__':
    loginMsg={
            'login_url':'http://if.fyi/xmlrpc.php',
            'login_usr':'if_fyi',
            'login_pw':'if_fyi',
            'wp_log':'if_fyi.log'
            }
    spParse=leaderShip(loginMsg)
    spParse.spiders_collect()
