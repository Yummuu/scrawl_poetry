# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders.crawl import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

from ImageSpider.items import ZgfItem
class ZgfSpider(CrawlSpider):
    name = 'zgf'
    allowed_domains = ['www.zhongguofeng.com']
    start_urls = [
        "https://www.zhongguofeng.com/jianzhu/",
        'https://www.zhongguofeng.com/pingmian/',
        "https://www.zhongguofeng.com/gufeng/",
        "https://www.zhongguofeng.com/yuanlin/",
        "https://www.zhongguofeng.com/fuzhuang/",
        "https://www.zhongguofeng.com/daojiao/",
        "https://www.zhongguofeng.com/fojiao/",
        "https://www.zhongguofeng.com/wenhua/",
    ]
    rules = [
        Rule(LinkExtractor(allow=r'https://www.zhongguofeng.com/[a-zA-Z]+?/list_[0-9]+?.html'), callback="parse_item", follow=True)
    ]
    def parse_item(self, response):
        item = ZgfItem()
        # imgurls = response.css("div.main div.img-demo img::attr(src)").extract()
        products = response.css("div.container div.product-border img::attr(src)").extract()
        banner = response.css("div.banner div.banner-img img::attr(src)").extract()
        imgurls = banner+products
        item['image_urls'] = imgurls
        # for img in item['image_urls']:
        #     print(img)
        #     pass
        yield item
        pass
