# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders.crawl import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from poetry.items import PoetryMoreItem

class mingjuRuleSpider(CrawlSpider):
    name = "mingjuRule"

    allowed_domains = ["so.gushiwen.cn","so.gushiwen.org"]
    start_urls = [
        "https://so.gushiwen.cn/mingju/",
        "https://so.gushiwen.cn/mingju/default.aspx?p=2&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=3&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=4&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=5&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=6&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=7&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=8&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=9&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=10&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=11&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=12&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=13&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=14&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=15&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=16&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=17&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=18&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=19&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=20&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=21&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=22&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=23&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=24&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=25&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=26&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=27&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=28&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=29&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=30&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=31&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=32&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=33&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=34&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=35&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=36&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=37&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=38&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=39&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=40&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=41&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=42&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=43&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=44&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=45&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=46&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=47&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=48&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=49&c=&t=",
        "https://so.gushiwen.cn/mingju/default.aspx?p=50&c=&t=",
        "https://so.gushiwen.org/shiwen/",
        "https://so.gushiwen.org/shiwen/default_0AA2.aspx",
        "https://so.gushiwen.org/shiwen/default_0AA3.aspx",
        "https://so.gushiwen.org/shiwen/default_0AA4.aspx",
        "https://so.gushiwen.org/shiwen/default_0AA5.aspx",
        "https://so.gushiwen.org/shiwen/default_0AA6.aspx",
        "https://so.gushiwen.org/shiwen/default_0AA7.aspx",
        "https://so.gushiwen.org/shiwen/default_0AA8.aspx",
        "https://so.gushiwen.org/shiwen/default_0AA9.aspx",
        "https://so.gushiwen.org/shiwen/default_0AA10.aspx",

        "https://so.gushiwen.cn/gushi/xiaoxue.aspx",
        "https://so.gushiwen.cn/gushi/chuzhong.aspx",
        "https://so.gushiwen.cn/gushi/gaozhong.aspx",
        "https://so.gushiwen.cn/gushi/tangshi.aspx",
        "https://so.gushiwen.cn/gushi/sanbai.aspx",
        "https://so.gushiwen.cn/gushi/songsan.aspx",
        "https://so.gushiwen.cn/gushi/songci.aspx",
        "https://so.gushiwen.cn/gushi/shijiu.aspx",
        "https://so.gushiwen.cn/gushi/shijing.aspx",
        "https://so.gushiwen.cn/gushi/chuci.aspx",
        "https://so.gushiwen.cn/gushi/yuefu.aspx",
        "https://so.gushiwen.cn/gushi/xiejing.aspx",
        "https://so.gushiwen.cn/gushi/yongwu.aspx",
        "https://so.gushiwen.cn/gushi/chuntian.aspx",
        "https://so.gushiwen.cn/gushi/xiatian.aspx",
        "https://so.gushiwen.cn/gushi/qiutian.aspx",
        "https://so.gushiwen.cn/gushi/dongtian.aspx",
        "https://so.gushiwen.cn/gushi/yu.aspx",
        "https://so.gushiwen.cn/gushi/xue.aspx",
        "https://so.gushiwen.cn/gushi/feng.aspx",
        "https://so.gushiwen.cn/gushi/hua.aspx",
        "https://so.gushiwen.cn/gushi/meihua.aspx",
        "https://so.gushiwen.cn/gushi/hehua.aspx",
        "https://so.gushiwen.cn/gushi/juhua.aspx",
        "https://so.gushiwen.cn/gushi/liushu.aspx",
        "https://so.gushiwen.cn/gushi/yueliang.aspx",
        "https://so.gushiwen.cn/gushi/shanshui.aspx",
        "https://so.gushiwen.cn/gushi/shan.aspx",
        "https://so.gushiwen.cn/gushi/shui.aspx",
        "https://so.gushiwen.cn/gushi/changjiang.aspx",
        "https://so.gushiwen.cn/gushi/huanghe.aspx",
        "https://so.gushiwen.cn/gushi/ertong.aspx",
        "https://so.gushiwen.cn/gushi/niao.aspx",
        "https://so.gushiwen.cn/gushi/ma.aspx",
        "https://so.gushiwen.cn/gushi/tianyuan.aspx",
        "https://so.gushiwen.cn/gushi/biansai.aspx",
        "https://so.gushiwen.cn/gushi/diming.aspx",
        "https://so.gushiwen.cn/gushi/jieri.aspx",
        "https://so.gushiwen.cn/gushi/chunjie.aspx",
        "https://so.gushiwen.cn/gushi/yuanxiao.aspx",
        "https://so.gushiwen.cn/gushi/hanshi.aspx",
        "https://so.gushiwen.cn/gushi/qingming.aspx",
        "https://so.gushiwen.cn/gushi/duanwu.aspx",
        "https://so.gushiwen.cn/gushi/qixi.aspx",
        "https://so.gushiwen.cn/gushi/zhongqiu.aspx",
        "https://so.gushiwen.cn/gushi/chongyang.aspx",
        "https://so.gushiwen.cn/gushi/huaigu.aspx",
        "https://so.gushiwen.cn/gushi/shuqing.aspx",
        "https://so.gushiwen.cn/gushi/aiguo.aspx",
        "https://so.gushiwen.cn/gushi/libie.aspx",
        "https://so.gushiwen.cn/gushi/songbie.aspx",
        "https://so.gushiwen.cn/gushi/sixiang.aspx",
        "https://so.gushiwen.cn/gushi/sinian.aspx",
        "https://so.gushiwen.cn/gushi/aiqing.aspx",
        "https://so.gushiwen.cn/gushi/lizhi.aspx",
        "https://so.gushiwen.cn/gushi/zheli.aspx",
        "https://so.gushiwen.cn/gushi/guiyuan.aspx",
        "https://so.gushiwen.cn/gushi/daowang.aspx",
        "https://so.gushiwen.cn/gushi/xieren.aspx",
        "https://so.gushiwen.cn/gushi/laoshi.aspx",
        "https://so.gushiwen.cn/gushi/muqin.aspx",
        "https://so.gushiwen.cn/gushi/youqing.aspx",
        "https://so.gushiwen.cn/gushi/zhanzheng.aspx",
        "https://so.gushiwen.cn/gushi/dushu.aspx",
        "https://so.gushiwen.cn/gushi/xishi.aspx",
        "https://so.gushiwen.cn/gushi/youguo.aspx",
        "https://so.gushiwen.cn/gushi/wanyue.aspx",
        "https://so.gushiwen.cn/gushi/haofang.aspx",
        "https://so.gushiwen.cn/gushi/minyao.aspx",
    ]
    rules = [
        Rule(LinkExtractor(allow=r'https://so.gushiwen.cn/shiwenv_[a-z0-9]+?.aspx'), callback="parse_item", follow=True),
        Rule(LinkExtractor(allow=r'https://so.gushiwen.org/shiwenv_[a-z0-9]+?.aspx'), callback="parse_item", follow=True)
    ]

    def parse_item(self, response):
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