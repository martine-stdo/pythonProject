import scrapy
import json
from heima_video.items import HeimaVideoItem


class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def __init__(self, *args, **kwargs):
        super(ItcastSpider, self).__init__(*args, **kwargs)
        self.items = []  # 将items初始化为一个实例变量

    def closed(self, reason):
        with open("teachers.json", "w", encoding="utf-8") as f:
            json.dump([item.as_dict()
            for item in self.items], f, ensure_ascii=False)

    def parse(self, response):
        for each in response.xpath("//div[@class='li_txt']"):
            item = HeimaVideoItem()  # 创建MyspiderItem类的对象
            name = each.xpath("h3/text()").extract()
            level = each.xpath("h4/text()").extract()
            resume = each.xpath("p/text()").extract()
            item["name"] = name[0]
            item["level"] = level[0]
            item["resume"] = resume[0]
            self.items.append(item)  # 修改此行，将items变为实例变量
