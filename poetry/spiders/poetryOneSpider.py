# -*- coding: utf-8 -*-

import scrapy

from poetry.items import PoetryItem

class poetryOneSpider(scrapy.Spider):
    name = "poetryOne"

    allowed_domains = ["www.shicimingju.com"]
    start_urls = [
        "http://www.shicimingju.com/chaxun/list/428077.html"
    ]

    def parse(self, response):
        print(response.status)
        if response.status==200:
            div_list = response.xpath('//div[@id="main_left"]')
            for div in div_list:
                title=div.xpath("./div[@id='item_div']/h1/text()").extract_first()
                link=response.url
                years=div.xpath("./div[@id='item_div']/div[@class='niandai_zuozhe']/text()").extract_first()
                author=div.xpath("./div[@id='item_div']/div[@class='niandai_zuozhe']/a/text()").extract_first()
                content=div.xpath("./div[@id='item_div']/div[@class='item_content']/text()").extract()
                description= response.xpath("string(//div[@id='item_shangxi']/div[@class='shangxi_content'])").extract()
                tags = div.xpath("./div[@id='item_div']/div[@class='shici-mark']/a/text()").extract()
                print(title,link,self.dealYears(years),author,self.dealContent(content),description,self.dealTags(tags))
                item=PoetryItem()
                item['title']=title
                item['link']=link
                item['years']=self.dealYears(years)
                item['author']=author
                item['content']=self.dealContent(content)
                item['description']=self.dealDescription(description)
                item['tags']=self.dealTags(tags)
                yield item
                pass
        pass

    def dealYears(self, years):
        if years:
            return years.replace('[','').replace(']','').replace(' ','')
        else:
            return '未知'
        pass

    def dealContent(self, content):
        strC = ''
        if len(content):
            for item in content:
                strC += item.replace('\n','').replace(' ','')+"</br>"
            return strC.strip('</br>')
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