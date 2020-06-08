# -*- coding: utf-8 -*-

import scrapy
import json
import requests

from scrapy.selector import Selector
from poetry.items import PoetryMoreItem

class mingjuOneSpider(scrapy.Spider):
    name = "mingjuOne"

    allowed_domains = ["so.gushiwen.org"]
    start_urls = [
        "https://so.gushiwen.org/shiwenv_c616fab1b377.aspx"
    ]

    def parse(self, response):
        fp=None
        fp=open("./liyulin.txt",'w',encoding='utf-8')
        # fp.write(response.text)
        # fp.close()
        title=response.xpath("//div[@class='main3']/div[@class='left']/div[2]/div[@class='cont']/h1/text()").extract_first()
        link=response.url
        source = response.xpath("//div[@class='main3']/div[@class='left']/div[2]/div[@class='cont']/p[@class='source']/a/text()").extract()
        if len(source)==2:
            years = source[0]
            author = source[1]
        else:
            years = '未知'
            author = '未知'
        content=response.xpath("string(//div[@class='main3']/div[@class='left']/div[2]/div[@class='cont']/div[@class='contson'])").extract()
        id_guid = response.xpath("//div[@class='main3']/div[@class='left']/div[2]/div[@class='cont']/div[@class='contson']/@id").extract_first()
        description= ''
        tags = response.xpath("//div[@class='main3']/div[@class='left']/div[2]/div[@class='tag']/a/text()").extract()
        # print(title,link,id_guid,source,self.dealTags(tags))
        # cookie={ 'Hm_lvt_04660099568f561a75456483228a9516':'1589253136,1589253397','Hm_lpvt_04660099568f561a75456483228a9516':'1589789247','login':'false'}
        # yi_response = requests.get('https://so.gushiwen.org/nocdn/ajaxshiwencont.aspx?id=%s&value=yi'%id_guid,cookies=cookie)
        # print(yi_response.text)
        # # fp.write(yi_response.content)
        # if yi_response.status_code==200:
        #     yi = yi_response.text
        # else:
        #     yi = '111'
        # fp.close()
        item=PoetryMoreItem()
        item['title']=title
        item['link']=link
        item['years']=years
        item['author']=author
        item['content']=self.dealContent(content)
        item['description']=self.dealDescription(description)
        item['tags']=self.dealTags(tags)
        item['id_guid']=id_guid
        item['yi'] = ''
        item['zhu'] = ''
        return item
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