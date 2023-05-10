import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from myDistributedSpider.items import MydistributedspiderItem
from scrapy_redis.spiders import RedisCrawlSpider


class ChanggouSpider(RedisCrawlSpider):
    name = 'chuanggou'
    allowed_domains = ['itheima.net']
    redis_key = 'chuanggou:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'pageNum=1000#glist|pageNum=[1-9]\d{0,2}#glist'), callback='parse_item', follow=True),
    )

    def parse(self, response):
        node_list = response.xpath('//div[@id="glist"]/ul/li/div')
        for node in node_list:
            # 将我们得到的数据封装到一个ChanggouItem对象
            item = MydistributedspiderItem()
            # extract()方法返回的都是Unicode字符串
            # 商品图片
            goods_pic = node.xpath('./div[1]/a/img/@src').getall()
            # 商品价格
            goods_price = node.xpath('./div[2]/strong/i/text()').getall()
            # 商品名称
            goods_name = node.xpath('./div[3]/a//text()').getall()
            # goods_name = node.xpath('./div[3]/a[string()]').getall()
            # 商品评价数
            goods_evaluation = node.xpath('./div[4]/i/span//text()').getall()
            item["goods_pic"] = goods_pic[0]
            item["goods_price"] = goods_price[0]
            item["goods_name"] = ''.join(goods_name).replace(' ', '')
            item["goods_evaluation"] = goods_evaluation[0]
            print(item)
            yield item
