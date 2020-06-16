# -*- coding: utf-8 -*-
import scrapy
from Lagou.Lagou.items import LagouItem


class LagoupositionSpider(scrapy.Spider):
    name = 'LagouPosition'
    allowed_domains = ['lagou.com']
    url = "https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91/p-city_2?px=default#filterBox"
    offset = 1
    start_urls = [url]

    # 将获取的信息发送给pipeline
    def parse(self, response):
        # 爬虫主要代码
        item = LagouItem()
        for line in response.xpath('//*[@id="s_position_list"]/ul/li[1]'):
            item['position_name'] = line.xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3')
            item['position_link'] = line.xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a')
            item['position_type'] = line.xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a')
            item['position_number'] = line.xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a')
            item['position_site'] = line.xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a')
            item['position_time'] = line.xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a')

            yield item

        yield scrapy.Request(url=self.start_urls, callback=self.parse)

