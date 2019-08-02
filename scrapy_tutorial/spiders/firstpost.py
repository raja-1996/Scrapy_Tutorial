# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider
from newsplease import NewsPlease
from bs4 import BeautifulSoup

class FirstpostSpider(SitemapSpider):
    name = 'firstpost'
    allowed_domains = ['firstpost.com']
    sitemap_urls = ['https://www.firstpost.com/feeds/sitemap/sitemapIndex.xml',
                    ]

    def parse(self, response):
        html = response.body
        article = NewsPlease.from_html(html)

        keywords = response.css('meta[name=news_keywords]::attr(content)').extract()
        subsection = ''
        articleSection = ''
        news_topics = response.css('.article-tags a::text').extract()



        # print(keywords)
        # print(article_tags)
        # print(article_section)

        temp = {
            'url': response.url,
            'title': article.title,
            'text': article.text,
            'description': article.description,
            'language': article.language,
            'date_publish': article.date_publish.strftime(
                "%m/%d/%Y, %H:%M:%S") if article.date_publish is not None else '',
            'date_modify': article.date_modify.strftime(
                "%m/%d/%Y, %H:%M:%S") if article.date_modify is not None else '',
            'authors': article.authors,
            'keywords': keywords,
            'subsection': subsection,
            'article_section': articleSection,
            'news_topics': news_topics,
        }
        # print(response.url)
        # if os.path.exists(topic_name+'/'+article.title+'.json'):
        #     print(topic_name+'/'+article.title+'.json')

        yield temp
