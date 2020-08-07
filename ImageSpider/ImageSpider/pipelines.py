# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class ImagespiderPipeline(object):
    
    fp=None
    def open_spider(self,spider):
        print('start')
        self.fp=open("./liyulin.txt",'w',encoding="utf-8")
        pass

    def process_item(self, item, spider):
        if spider.name=='zgf':
            for link in item['image_urls']:
                self.fp.write(link+'\n')
                pass
        elif spider.name=='zgfOne':
            for link in item['image_urls']:
                self.fp.write(link+'\n')
                pass
        return item['image_urls']

    def close_spider(self, spider):
        self.fp.close()
        print('end')
        pass
    # def get_media_requests(self, item, info):
    #     yield scrapy.Request(url=item['image_urls'])