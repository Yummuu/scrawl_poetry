# -*- coding: utf-8 -*-
import scrapy

from ImageSpider.items import ZgfItem
class ZgfOneSpider(scrapy.Spider):
    name = 'zgfOne'
    allowed_domains = ['www.zhongguofeng.com']
    start_urls = [
        "http://www.zhongguofeng.com/"
    ]
    def parse(self, response):
        item = ZgfItem()
        imgurls = response.css("div.main div.img-demo img::attr(src)").extract()
        item['image_urls'] = imgurls
        for img in imgurls:
            print(img)
            pass
        yield item
        pass
