# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

class FlipkartSpider(scrapy.Spider):
    name = 'flipkart'
    allowed_domains = ['flipkart.com']
    start_urls = ['http://flipkart.com/']

    def parse(self, response):
        # links = response.css('a::attr(href)').extract()

        links_ = LinkExtractor().extract_links(response)
        # print([x.url for x in links_])
        yield {'links': [x.url for x in links_]}

