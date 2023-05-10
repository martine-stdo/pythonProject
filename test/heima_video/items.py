# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HeimaVideoItem(scrapy.Item):
    name = scrapy.Field()
    level = scrapy.Field()
    resume = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    def as_dict(self):
        return dict(self)
