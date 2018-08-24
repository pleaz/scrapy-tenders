# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class TendersPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):

    #collection_name = 'linked'
    #collection_name = 'test'
    collection_name = 'tenders'

    def __init__(self, mongo_server, mongo_port, mongo_db, mongo_collection):
        self.mongo_server = 'localhost'
        self.mongo_port = 27017
        self.mongo_db = 'parsing'
        #self.mongo_collection = 'linked'
        #self.mongo_collection = 'test'
        self.mongo_collection = 'tenders'


    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_server=crawler.settings.get('MONGODB_SERVER'),
            mongo_port=crawler.settings.get('MONGODB_PORT'),
            mongo_db=crawler.settings.get('MONGODB_DB'),
            mongo_collection=crawler.settings.get('MONGODB_COLLECTION'),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_server, self.mongo_port)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item