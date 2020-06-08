# -*- coding: utf-8 -*-

import scrapy

from poetry.items import PoetryItem

class poetrySpider(scrapy.Spider):
    name = "poetry"

    allowed_domains = ["www.shicimingju.com"]
    start_urls = [
        "http://www.shicimingju.com/chaxun/list/2810.html"
    ]
    url = "http://www.shicimingju.com/chaxun/list/%d.html"
    htmlNum = 2810
    maxNum = 428077
    #简单的遍历
    def parse(self, response):
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
            if self.htmlNum<=self.maxNum:
                print("%d is finish"%self.htmlNum)
                self.htmlNum+=1
                new_url=format(self.url%self.htmlNum)
                yield scrapy.Request(url=new_url, callback=self.parse)
        else:
            if self.htmlNum<=self.maxNum:
                self.htmlNum+=1
                new_url=format(self.url%self.htmlNum)
                yield scrapy.Request(url=new_url, callback=self.parse)
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