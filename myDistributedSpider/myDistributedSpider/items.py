# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MydistributedspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 商品图片链接
    goods_pic = scrapy.Field()
    # 商品价格
    goods_price = scrapy.Field()
    # 商品名称
    goods_name = scrapy.Field()
    # 商品评价数
    goods_evaluation = scrapy.Field()
