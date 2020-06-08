# -*- coding: utf-8 -*-

import scrapy
import json
import requests

from scrapy.selector import Selector
from poetry.items import AuthorItem

class authorOneSpider(scrapy.Spider):
    name = "authorOne"

    allowed_domains = ["so.gushiwen.cn"]
    start_urls = [
        "https://so.gushiwen.cn/authorv_9cb3b7c0e4a0.aspx"
    ]

    def parse(self, response):
        link=response.url
        author=response.xpath("//div[@class='main3']/div[@class='left']/div[2]/div[@class='cont']/h1/span/b/text()").extract_first()
        description=response.xpath("//div[@class='main3']/div[@class='left']/div[1]/textarea/text()").extract_first()
        item=AuthorItem()
        item['link']=link
        item['years']=''
        item['author']=author
        item['description']=description
        item['content']=''
        return item
        pass
