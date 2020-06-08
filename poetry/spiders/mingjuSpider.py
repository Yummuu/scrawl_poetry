# -*- coding: utf-8 -*-

import scrapy
import json
import requests

from scrapy.selector import Selector
from poetry.items import PoetryMoreItem

class mingju(scrapy.Spider):
    name = "mingju"

    allowed_domains = ["so.gushiwen.cn"]
    start_urls = []

    def parse(self, response):
        pass
