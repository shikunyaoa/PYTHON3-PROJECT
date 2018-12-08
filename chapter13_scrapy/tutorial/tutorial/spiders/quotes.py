# -*- coding: utf-8 -*-
import scrapy

from chapter13_scrapy.tutorial.tutorial.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    # 项目唯一的名字
    name = 'quotes'
    # 允许爬取的域名，如果请求链接不是这个域名下的，则请求会被过滤掉
    allowed_domains = ['quotes.toscrape.com']
    # Spider在启动时爬取的url列表，初始请求是由它来定义的
    start_urls = ['http://quotes.toscrape.com/']
    # 返回的响应作为参数
    # 该方法负责解析返回的响应，提取数据或者进一步生成要处理的请求
    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()
            item["text"] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item

        next = response.css('.pager .next a::attr("href")').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)