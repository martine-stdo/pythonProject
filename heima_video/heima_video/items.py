# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HeimaVideoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    video_name = scrapy.Field()     # 视频名称
    video_detail = scrapy.Field()   # 视频描述
    students = scrapy.Field()       # 学习人数
    video_link = scrapy.Field()     # 视频链接
