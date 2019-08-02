# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider

class FlipkartRobotsSpider(SitemapSpider):
    name = 'flipkart_robots'
    sitemap_urls = ['https://docs.scrapy.org/robots.txt']

    def parse(self, response):
        print(response.url)
        yield {'link': response.url}
