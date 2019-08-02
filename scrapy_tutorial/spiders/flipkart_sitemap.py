# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider


class FlipkartSitemapSpider(SitemapSpider):
    name = 'flipkart_sitemap'
    sitemap_urls = ['http://www.flipkart.com/sitemap_p_product_index_1.xml']

    def parse(self, response):
        print(response.url)
        yield {'link': response.url}


from scrapy_proxy_pool.middlewares import BanDetectionMiddleware