# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors

class PoetryPipeline(object):
    
    fp=None
    def open_spider(self,spider):
        print('start')
        self.fp=open("./liyulin.txt",'w',encoding="utf-8")
        pass

    def process_item(self, item, spider):
        self.fp.write(item["title"]+":"+item["link"]+'\n')
        return item

    def close_spider(self, spider):
        self.fp.close()
        print('end')
        pass
