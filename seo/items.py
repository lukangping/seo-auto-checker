# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SeoItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    title = scrapy.Field()
    h1 = scrapy.Field()
    desc = scrapy.Field()

class ExpectedSeo:
	def __init__(self, url, title, h1, desc):
		self.url = url
		self.title = title
		self.h1 = h1
		self.desc = desc
