import scrapy
from heima_video.items import HeimaVideoItem


class HeimaSpider(scrapy.Spider):
    name = "heima"
    allowed_domains = ["heima_video.cn"]
    start_urls = ['http://yun.itheima.com/course/c144.html']

    def parse(self, response):
        items = []  # 存储视频信息
        node_list = response.xpath('//div[contains(@class,"spjclist") and contains(@class,"spjclist1")]//ul[2]/li/a')
        basic_url = 'http://yun.itheima.com'
        for each in node_list:
            # 创建HeimaVideoItem类的对象
            item = HeimaVideoItem()
            # 使用Xpath的路径表达式选取节点
            video_name = each.xpath("./div[2]/h2/text()").getall()  # 视频名称
            video_detail = each.xpath("./div[2]/p/text()").getall()  # 视频描述
            students = each.xpath("./div[3]/p/span/text()").getall()  # 学习人数
            video_link = each.xpath("./@href").getall()  # 视频链接
            # 将每个视频的信息封装成HeimaVideoItem类的对象
            item["video_name"] = video_name[0]
            item["video_detail"] = video_detail[0]
            item["students"] = students[0]
            item["video_link"] = basic_url + video_link[0]
            items.append(item)
        return items