# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders.crawl import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

from poetry.items import PoetryItem

class poetryRuleSpider(CrawlSpider):
    name = "poetryRule"

    allowed_domains = ["www.shicimingju.com"]
    start_urls = [
        "http://www.shicimingju.com"
    ]
    rules = [
        Rule(LinkExtractor(allow=r'http://www.shicimingju.com/chaxun/list/[0-9]+?.html'), callback="parse_item", follow=True)
    ]
     #根据rule遍历
    def parse_item(self, response):
        title=response.xpath("//div[@id='main_left']/div[@id='item_div']/h1/text()").extract_first()
        link=response.url
        years=response.xpath("//div[@id='main_left']/div[@id='item_div']/div[@class='niandai_zuozhe']/text()").extract_first()
        author=response.xpath("//div[@id='main_left']/div[@id='item_div']/div[@class='niandai_zuozhe']/a/text()").extract_first()
        content=response.xpath("string(//div[@id='item_div']/div[@class='item_content'])").extract()
        description= response.xpath("string(//div[@id='item_shangxi']/div[@class='shangxi_content'])").extract()
        tags = response.xpath("//div[@id='main_left']/div[@id='item_div']/div[@class='shici-mark']/a/text()").extract()
        item=PoetryItem()
        item['title']=title
        item['link']=link
        item['years']=self.dealYears(years)
        item['author']=author
        item['content']=self.dealContent(content)
        item['description']=self.dealDescription(description)
        item['tags']=self.dealTags(tags)
        return item
        pass

    def dealYears(self, years):
        if years:
            return years.replace('[','').replace(']','').replace(' ','')
        else:
            return '未知'
        pass

    def dealContent(self, content):
        if len(content):
            return content[0].strip("\n").strip(" ")
        else:
            return ''
        pass

    def dealTags(self, tags):
        return ','.join(tags)
        pass

    def dealDescription(self, description):
        if len(description):
            return description[0].strip("\n").strip(" ")
        else:
            return ''
        pass