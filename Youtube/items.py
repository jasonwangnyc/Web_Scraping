# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YoutubeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Username = scrapy.Field()
    Uploads = scrapy.Field()
    Subscribers = scrapy.Field()
    Views = scrapy.Field()
    Country = scrapy.Field()
    Type = scrapy.Field()
    Created_Date = scrapy.Field()
    Subscribe_Rank = scrapy.Field()
    Views_Rank = scrapy.Field()
    Estimated_Yearly_Earning = scrapy.Field()