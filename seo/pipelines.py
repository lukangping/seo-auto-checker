import csv
import re
from seo.items import SeoItem, ExpectedSeo

class SeoVerifyPipeline(object):

	expected_seos = {}

	def __init__(self):
		reader = csv.reader(open("seo/csv/#354-1.csv"), delimiter=",")
		for url,title,h1,desc in reader:
			seo = ExpectedSeo(url, title, h1, desc)
			self.expected_seos[str(url)] = seo

	def process_item(self, item, spider):
		parsed_title = item["title"]
		parsed_h1 = item["h1"]
		if "desc" in item:
			parsed_desc = item["desc"]
		else:
			parsed_desc = "blank"

		expected_title = self.expected_seos[item["url"]].title
		expected_h1 = self.expected_seos[item["url"]].h1
		expected_desc = self.expected_seos[item["url"]].desc

		if parsed_title != expected_title:
			print "------"
			print "title parsed   :" + item["title"].encode('utf-8') + "."
			print "title expected :" + expected_title.encode('utf-8') + "."
			print "title wrong url:" + item["url"].encode('utf-8')
		
		if not expected_h1 in parsed_h1:
			print "------"
			print "h1 parsed   :" + item["h1"].encode('utf-8') + "."
			print "h1 expected :" + expected_h1.encode('utf-8') + "."
			print "h1 wrong url:" + item["url"].encode('utf-8')

		if parsed_desc != expected_desc:
			print "------"
			print "desc parsed:   " + parsed_desc.encode('utf-8') + "."
			print "desc expected: " + expected_desc.encode('utf-8') + "."
			print "desc wrong url:" + item["url"].encode('utf-8') + "."
		
		return item