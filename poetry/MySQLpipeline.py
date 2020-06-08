# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class MySQLPipeline(object):

    def __init__(self):
        self.connect = MySQLdb.connect(
            host='localhost',
            db='liyulin',
            user='root',
            passwd='liyulin',
            charset='utf8',
            use_unicode=True)
            # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
        pass

    def process_item(self, item, spider):
        if spider.name=='mingju':
            self.cursor.execute(
                """insert into poetry_v3 (title, link,years,author,content,description,tags,id_guid,yi,zhu) value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (item['title'],item['link'],item['years'],item['author'],item['content'],item['description'],item['tags'],item['id_guid'],item['yi'],item['zhu'],)
            )
            self.connect.commit()
        elif spider.name=='authorRule':
            self.cursor.execute(
                """insert into poetry_author_detail (link,years,author,content,description) value (%s, %s, %s, %s, %s)""",
                (item['link'],item['years'],item['author'],item['content'],item['description'],)
            )
            self.connect.commit()
        else:
            self.cursor.execute(
                """insert into poetry_v2 (title, link,years,author,content,description,tags) value (%s, %s, %s, %s, %s, %s, %s)""",
                (item['title'],item['link'],item['years'],item['author'],item['content'],item['description'],item['tags'],)
            )
            self.connect.commit()
        return item
