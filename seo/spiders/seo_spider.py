#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
import re
import csv
import sys  

reload(sys)  
sys.setdefaultencoding('utf-8')  

from seo.items import SeoItem, ExpectedSeo

class SeoSpider(scrapy.Spider):
	
	name = "seo"

	def __init__(self, *args, **kwargs): 
		super(SeoSpider, self).__init__(*args, **kwargs) 		
		
		reader = csv.reader(open("seo/csv/#354-1.csv"), delimiter=",")
		for url,title,h1,desc in reader:
			self.start_urls.append(str(url))

	def parse(self, response):
		item = SeoItem()
		item["url"]=response.url
		title=response.xpath("//title/text()").extract()[0]
		item["title"]=re.sub(r'\xa0',' ', title)
		item["h1"]=response.xpath("//h1/text()").extract()[0]
		# print item["url"]
		# print item["title"]
		# print item["h1"]

		# if response.xpath('//meta[@name="description"]'):
		item["desc"]=str(response.xpath('//meta[@name="description"]/@content').extract()[0])

		yield item