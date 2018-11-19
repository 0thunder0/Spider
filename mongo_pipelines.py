import pymongo
class MongoPipeline(object):
    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri=mongo_uri
        self.mongo_db=mongo_db
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
            )
    # crawler这个抓取器读取settings.py 文件中的MONGO_URI,MONGO_DATABASE 两个值返回
    def open_spider(self,spider):
        self.client=pymongo.MongoClient(self.mongo_uri)
        self.db=self.client[self.mongo_db]
    def close_spider(self,spider):
        self.client.close()
        #open_spider和close_spider 作用是让mongo 随着爬虫的打开而打开，关闭而关闭
    def process_item(self,item,spider):
        # 每生成一个item数据，就用process_item这个函数来执行
        collection_name=item.__class__.__name__
        # 定义 mongo里面的表名
        self.db[collection_name].insert(dict(item))
        return item
