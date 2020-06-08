# -*- coding: utf-8 -*-

import scrapy

from scrapy.spiders.crawl import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from poetry.items import AuthorItem

class authorRuleSpider(CrawlSpider):
    name = "authorRule"

    allowed_domains = ["so.gushiwen.cn"]
    start_urls = [
        "https://so.gushiwen.cn/authors/Default.aspx?p=1&c=先秦",
        "https://so.gushiwen.cn/authors/Default.aspx?p=2&c=先秦",
        "https://so.gushiwen.cn/authors/Default.aspx?p=3&c=先秦",
        "https://so.gushiwen.cn/authors/Default.aspx?p=4&c=先秦",
        "https://so.gushiwen.cn/authors/Default.aspx?p=5&c=先秦",
        "https://so.gushiwen.cn/authors/Default.aspx?p=6&c=先秦",
        "https://so.gushiwen.cn/authors/Default.aspx?p=7&c=先秦",
        "https://so.gushiwen.cn/authors/Default.aspx?p=8&c=先秦",
        "https://so.gushiwen.cn/authors/Default.aspx?p=9&c=先秦",
        "https://so.gushiwen.cn/authors/Default.aspx?p=10&c=先秦",

        "https://so.gushiwen.cn/authors/Default.aspx?p=1&c=两汉",
        "https://so.gushiwen.cn/authors/Default.aspx?p=2&c=两汉",
        "https://so.gushiwen.cn/authors/Default.aspx?p=3&c=两汉",
        "https://so.gushiwen.cn/authors/Default.aspx?p=4&c=两汉",
        "https://so.gushiwen.cn/authors/Default.aspx?p=5&c=两汉",
        "https://so.gushiwen.cn/authors/Default.aspx?p=6&c=两汉",
        "https://so.gushiwen.cn/authors/Default.aspx?p=7&c=两汉",
        "https://so.gushiwen.cn/authors/Default.aspx?p=8&c=两汉",
        "https://so.gushiwen.cn/authors/Default.aspx?p=9&c=两汉",
        "https://so.gushiwen.cn/authors/Default.aspx?p=10&c=两汉",

        "https://so.gushiwen.cn/authors/Default.aspx?p=1&c=魏晋",
        "https://so.gushiwen.cn/authors/Default.aspx?p=2&c=魏晋",
        "https://so.gushiwen.cn/authors/Default.aspx?p=3&c=魏晋",
        "https://so.gushiwen.cn/authors/Default.aspx?p=4&c=魏晋",
        "https://so.gushiwen.cn/authors/Default.aspx?p=5&c=魏晋",
        "https://so.gushiwen.cn/authors/Default.aspx?p=6&c=魏晋",
        "https://so.gushiwen.cn/authors/Default.aspx?p=7&c=魏晋",
        "https://so.gushiwen.cn/authors/Default.aspx?p=8&c=魏晋",
        "https://so.gushiwen.cn/authors/Default.aspx?p=9&c=魏晋",
        "https://so.gushiwen.cn/authors/Default.aspx?p=10&c=魏晋",

        "https://so.gushiwen.cn/authors/Default.aspx?p=1&c=南北朝",
        "https://so.gushiwen.cn/authors/Default.aspx?p=2&c=南北朝",
        "https://so.gushiwen.cn/authors/Default.aspx?p=3&c=南北朝",
        "https://so.gushiwen.cn/authors/Default.aspx?p=4&c=南北朝",
        "https://so.gushiwen.cn/authors/Default.aspx?p=5&c=南北朝",
        "https://so.gushiwen.cn/authors/Default.aspx?p=6&c=南北朝",
        "https://so.gushiwen.cn/authors/Default.aspx?p=7&c=南北朝",
        "https://so.gushiwen.cn/authors/Default.aspx?p=8&c=南北朝",
        "https://so.gushiwen.cn/authors/Default.aspx?p=9&c=南北朝",
        "https://so.gushiwen.cn/authors/Default.aspx?p=10&c=南北朝",

        "https://so.gushiwen.cn/authors/Default.aspx?p=1&c=隋代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=2&c=隋代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=3&c=隋代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=4&c=隋代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=5&c=隋代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=6&c=隋代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=7&c=隋代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=8&c=隋代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=9&c=隋代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=10&c=隋代",

        "https://so.gushiwen.cn/authors/Default.aspx?p=1&c=唐代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=2&c=唐代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=3&c=唐代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=4&c=唐代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=5&c=唐代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=6&c=唐代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=7&c=唐代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=8&c=唐代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=9&c=唐代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=10&c=唐代",

        "https://so.gushiwen.cn/authors/Default.aspx?p=1&c=五代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=2&c=五代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=3&c=五代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=4&c=五代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=5&c=五代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=6&c=五代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=7&c=五代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=8&c=五代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=9&c=五代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=10&c=五代",

        "https://so.gushiwen.cn/authors/Default.aspx?p=1&c=宋代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=2&c=宋代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=3&c=宋代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=4&c=宋代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=5&c=宋代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=6&c=宋代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=7&c=宋代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=8&c=宋代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=9&c=宋代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=10&c=宋代",

        "https://so.gushiwen.cn/authors/Default.aspx?p=1&c=金朝",
        "https://so.gushiwen.cn/authors/Default.aspx?p=2&c=金朝",
        "https://so.gushiwen.cn/authors/Default.aspx?p=3&c=金朝",
        "https://so.gushiwen.cn/authors/Default.aspx?p=4&c=金朝",
        "https://so.gushiwen.cn/authors/Default.aspx?p=5&c=金朝",
        "https://so.gushiwen.cn/authors/Default.aspx?p=6&c=金朝",
        "https://so.gushiwen.cn/authors/Default.aspx?p=7&c=金朝",
        "https://so.gushiwen.cn/authors/Default.aspx?p=8&c=金朝",
        "https://so.gushiwen.cn/authors/Default.aspx?p=9&c=金朝",
        "https://so.gushiwen.cn/authors/Default.aspx?p=10&c=金朝",

        "https://so.gushiwen.cn/authors/Default.aspx?p=1&c=元代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=2&c=元代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=3&c=元代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=4&c=元代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=5&c=元代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=6&c=元代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=7&c=元代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=8&c=元代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=9&c=元代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=10&c=元代",

        "https://so.gushiwen.cn/authors/Default.aspx?p=1&c=明代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=2&c=明代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=3&c=明代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=4&c=明代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=5&c=明代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=6&c=明代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=7&c=明代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=8&c=明代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=9&c=明代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=10&c=明代",

        "https://so.gushiwen.cn/authors/Default.aspx?p=1&c=清代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=2&c=清代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=3&c=清代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=4&c=清代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=5&c=清代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=6&c=清代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=7&c=清代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=8&c=清代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=9&c=清代",
        "https://so.gushiwen.cn/authors/Default.aspx?p=10&c=清代",
    ]
    rules = [
        Rule(LinkExtractor(allow=r'https://so.gushiwen.cn/authorv_[a-z0-9]+?.aspx',deny=r'https://so.gushiwen.cn/authorv_[0-9]+?.aspx'), callback="parse_item", follow=True)
    ]
    def parse_item(self, response):
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
