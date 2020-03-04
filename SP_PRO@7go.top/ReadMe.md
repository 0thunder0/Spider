# 采集程序统一

## 运行环境：

```python
pip install python-wordpress-xmlrpc zhconv pyquery apscheduler

```

## 数据采集模块：
### 数据输出：

sourceUrl,title,featureImg,plot,category,tags,customField

    +   文章源网址(字符串)：sourceUrl
    +   标题(字符串)：title
    +   特色图片(字符串)：featureImg
    +   文章内容(字符串)：content
    +   分类(列表)：category
    +   标签(列表)：tags
    +   自定义字段(字典):customField
        -   图片合集(列表)：imgList
        -   下载资源(字符串)：downloadArea
    +   文章形式(字符串):postForm

### 采集模块函数：

    +   执行分类采集：categoryParse
    +   执行内容采集：entryParse

## 发布模块:wpXmlrpc
    wpXmlrpc
    发布/编辑文章：editPost
        editPost(self,postID,sourceUrl,title,featureImg,content,category,tags,customField)
        postID='0'  发布文章，不等于'0' 编辑文章
        return postID
    删除文章：trashPost
        trashPost(postIDs) #postIDs 列表
    查看文章：checkPost

    下载远程图片：downImgs
        downImgs(postID,imgList,localAbspath)
        return new_imgList
    删除本地图片：trashImg