# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ScrapyTutorialItem


class SpeakerSpider(CrawlSpider):
    name = 'speaker'
    allowed_domains = ['flipkart.com']
    start_urls = ['https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7']

    rules = (
        Rule(LinkExtractor(restrict_css='._3fVaIS'), follow=True, callback='parse_item'),
        # Rule(LinkExtractor(), callback='parse_item'),
    )

    def parse_item_(self, response):
        print(response.url)

    def parse_start_url(self, response):
        # pass
        item = ScrapyTutorialItem()

        titles = response.css('._2cLu-l::text').extract()
        count_reviews = response.css('._38sUEc::text').extract()

        item['url'] = response.url
        item['titles'] = titles
        item['count_reviews'] = count_reviews

        yield item

    def parse_item(self, response):
        print(response.url)
        item = ScrapyTutorialItem()

        titles = response.css('._2cLu-l::text').extract()
        count_reviews = response.css('._38sUEc::text').extract()

        item['url'] = response.url
        item['titles'] = titles
        item['count_reviews'] = count_reviews

        yield item

        # cc = LinkExtractor( restrict_css='.a-last').extract_links(response)
        # for link in cc:
        #     print(link.url)
