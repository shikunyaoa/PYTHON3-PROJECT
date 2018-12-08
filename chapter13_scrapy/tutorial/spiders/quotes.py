# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import QuoteItem


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
        # response.css()返回的是一个Selectorlist类型
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()
            # 使用extract或extract_first才能把真实需要的内容获取下来
            # extract_first:用来提取Selectorlist第一个元素
            # 如果Selectorlist为空，extract_first会返回空，不会报错
            item["text"] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            # 使用extract获取没有元素的空Selectorlist会导致数组越界
            # extract_first解决了此问题
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item

        next = response.css('.pager .next a::attr("href")').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)