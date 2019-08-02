# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ScrapyTutorialItem



class AmazonSpider(CrawlSpider):
    name = 'amazon'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/s?k=Over-Ear&i=electronics&rh=n%3A976419031%2Cn%3A14146390031&dc&qid=1564727505&rnid=976420031&ref=sr_nr_n_1']

    rules = (
        Rule(LinkExtractor(restrict_css='.a-last a'),  follow=True, callback='parse_item'),
        # Rule(LinkExtractor(), callback='parse_item'),
    )


    def parse_item_(self, response):
        print(response.url)


    def parse_start_url(self, response):
        # pass
        item = ScrapyTutorialItem()

        titles = response.css('.a-color-base.a-text-normal::text').extract()
        count_reviews = response.css('.a-size-small .a-size-base::text').extract()

        item['url'] = response.url
        item['titles'] = titles
        item['count_reviews'] = count_reviews

        yield item


    def parse_item(self, response):
        print(response.url)
        item = ScrapyTutorialItem()

        titles = response.css('.a-color-base.a-text-normal::text').extract()
        count_reviews = response.css('.a-size-small .a-size-base::text').extract()

        item['url'] = response.url
        item['titles'] = titles
        item['count_reviews'] = count_reviews

        yield item




        # cc = LinkExtractor( restrict_css='.a-last').extract_links(response)
        # for link in cc:
        #     print(link.url)
