# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    position_name = scrapy.Field()
    position_link = scrapy.Field()
    position_type = scrapy.Field()
    position_number = scrapy.Field()
    position_site = scrapy.Field()
    position_time = scrapy.Field()

