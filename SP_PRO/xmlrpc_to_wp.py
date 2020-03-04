import urllib,os,time,random,zhconv,shutil
from wordpress_xmlrpc import Client,WordPressPost,WordPressTerm
from wordpress_xmlrpc.methods.posts import GetPost,NewPost,EditPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import taxonomies,posts,media
from wordpress_xmlrpc.compat import xmlrpc_client

class wpXmlrpc:
    def __init__(self,*args):
        loginMsg=args[0]
        self.loginUrl=loginMsg["login_url"]
        self.login_usr=loginMsg["login_usr"]
        self.login_pw=loginMsg["login_pw"]
        if loginMsg["wp_log"]:
            self.wp_log=loginMsg["wp_log"]
            if not os.path.isfile(self.wp_log):
                os.mknod(self.wp_log)        
        self.wp=self.login_func()

    def login_func(self): 
        wp=Client(self.loginUrl,self.login_usr,self.login_pw)
        return wp
#传递过来的数据：sourceUrl,title,featureImg,plot,category,tags,customField
    def editPost(self,postID,sourceUrl,title,featureImg,content,category,tags,customField):
        post = WordPressPost()
        post.title=title #标题
        post.content=content #内容
        #post.post_status = 'publish' 
        #文章状态，不写默认是草稿，private表示私密的，draft表示草稿，publish表示发布
        imgList=[] #图片列表
        if customField != {}:
            try:
                if customField["imgList"]:
                    imgList=customField["imgList"]
                else:
                    imgList=str(imgList)
            except KeyError:
                print("customField中没有imgList这个图片列表")

        if not category:
            category=['other',]
        post.categrory=category

        if tags:
            post.terms_names={
                'post_tag':tags, #文章所属标签，没有则自动创建
                'category':post.categrory #文章所属分类，没有则自动创建
            }
        else:
            post.terms_names={
                'post_tag':'',
                'category':post.categrory
            }

        #自定义字段列表
        post.custom_fields = []
        #添加自定义字段内容
        if postID =='0':
            for key in customField:
                post.custom_fields.append({
                    'key': key,
                    'value': customField[key]
                })
                #print('post.custom_fields',type(post.custom_fields),post.custom_fields)
        else:
            for n in range(len(post.custom_fields)):
                for key in customField:
                    if post.custom_fields[n]['key']== key and post.custom_fields[n]['value'] != customField[key]:
                        post.custom_fields[n]['value'] = customField[key]

        #如果特色图片存在，上传特色图片
        if featureImg:
            img_name=featureImg.split('/')[-1]
            filename =featureImg
            data = {
                    'name': img_name,
                    'type': 'image/jpeg'
                }
            with open(filename, 'rb') as img:
                data['bits'] = xmlrpc_client.Binary(img.read())
            response=self.wp.call(media.UploadFile(data))
            attachment_id = response['id']
            post.thumbnail=attachment_id
        if postID == '0':
            postID = self.wp.call(NewPost(post))        
            print('正在发布[ID]:%s,[标题]:%s' %(postID,post.title))
        else:
            self.wp.call(EditPost(postID,post))
            print('正在修正[ID]:%s,[标题]:%s' %(postID,post.title))
        return postID

    def trashPost(self,postIDs):
        for postID in postIDs:
            post = WordPressPost()
            #根据ID查看文章
            try:
                plot=self.wp.call(GetPost(postID))
                # print('删除文章:',plot,type(plot),plot.title)
                post.title=plot.title
                post.post_status ='trash'            
                self.wp.call(EditPost(postID,post))
                print('已删除文章[ID]:[%s],[标题]:%s' %(postID,plot.title))
            except:
                print('文章[ID]:[%s],已经被删除,请不要重复删' %postID)

    #下载图片到otl.ooo这域名下
    def downImgs(self,postID,imgList,localAbspath):
        if type(postID) is not str:
            postID=str(postID)
        if not os.path.isdir(localAbspath):
            os.makedirs(localAbspath)
        #判断偷拍你格式是列表还是字符串，并下载图片到本地    
        if type(imgList) is str:
            new_imgList=''
            newImgUrl=imgList.split('!')[0]
            print('开始下载图片:%s' %newImgUrl)
            imgLocalPath=localAbspath+postID
            imgLocalAbsolutePath=imgLocalPath+'/'+newImgUrl.split('?')[0].split('/')[-1]
            if not os.path.isdir(imgLocalPath):
                os.makedirs(imgLocalPath)
            try:
                urllib.request.urlretrieve(newImgUrl,imgLocalAbsolutePath)
            except:
                print('图片下载失败:',newImgUrl)
            new_imgList=imgLocalAbsolutePath
        else:
            new_imgList=[]        
            for img_url in imgList:
                img_url=img_url.split('!')[0]
                print('开始下载图片:%s' %img_url)
                imgLocalPath=localAbspath+postID
                imgLocalAbsolutePath=imgLocalPath+'/'+img_url.split('?')[0].split('/')[-1]
                #print('图片保存地址：',img_url,imgLocalPath,imgLocalAbsolutePath)
                if not os.path.isdir(imgLocalPath):
                    os.makedirs(imgLocalPath)
                try:
                    urllib.request.urlretrieve(img_url,imgLocalAbsolutePath)
                except:
                    print('图片下载失败:',img_url)
                #new_imgList.append(imgLocalAbsolutePath.replace('/www/wwwroot/','http://'))
                new_imgList.append(imgLocalAbsolutePath)

        return new_imgList

    #删除制定目录
    def trashImg(self,postID):
        path='/www/wwwroot/otl.ooo/IMAGE/'+str(postID)
        shutil.rmtree(path)

if __name__=='__main__':
    loginMsg={
            'login_url':'http://if.fyi:1180/xmlrpc.php',
            'login_usr':'if_fyi',
            'login_pw':'if_fyi',
            'wp_log':'if-fyi.log'
            }
    wp=wpXmlrpc(loginMsg)
    sourceUrl=''
    randInt=random.randint(0,23330)
    postID='54'
    title='第九百一十五章 你父亲有私生子吗？'+str(randInt)
    featureImg='./20191103014021_c96606de4fc122eec1cdb21479972d1a_1.jpeg'
    content='丙辰中秋，欢饮达旦，大醉，作此篇，兼怀子由。 明月几时有？把酒问青天。不知天上宫阙，今夕是何年。我欲乘风归去，又恐琼楼玉宇，高处不胜寒。起舞弄清影，何似在人间？    转朱阁，低绮户，照无眠。不应有恨，何事长向别时圆？人有悲欢离合，月有阴晴圆缺，此事古难全。但愿人长久，千里共婵娟。'
    category=['OTHER']
    tags=['hahaha',]
    customField={"作者":'近者',"时间":'20191124'}
    #wp.editPost(postID,sourceUrl,title,featureImg,content,category,tags,customField)
    #删除指定ID文章
    postIDs=['54','29','26','22','18']
    wp.trashPost(postIDs)
