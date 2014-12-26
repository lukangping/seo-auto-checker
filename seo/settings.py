# -*- coding: utf-8 -*-

# Scrapy settings for seo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'seo'

SPIDER_MODULES = ['seo.spiders']
NEWSPIDER_MODULE = 'seo.spiders'

ITEM_PIPELINES = {	
    'seo.pipelines.SeoVerifyPipeline': 800,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'seo (+http://www.yourdomain.com)'
