# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider
from newsplease import NewsPlease
from bs4 import BeautifulSoup

class News18Spider(SitemapSpider):
    name = 'news18'

    allowed_domains = ['news18.com']
    sitemap_urls = ['https://www.news18.com/text-sitemap-2019-index.xml',
                    'https://www.news18.com/text-sitemap-2018-index.xml',
                    'https://www.news18.com/text-sitemap-2017-index.xml',
                    'https://www.news18.com/text-sitemap-2016-index.xml',
                    'https://www.news18.com/text-sitemap-2015-index.xml',
                    'https://www.news18.com/text-sitemap-2014-index.xml',
                    'https://www.news18.com/text-sitemap-2013-index.xml',
                    'https://www.news18.com/text-sitemap-2012-index.xml',
                    'https://www.news18.com/text-sitemap-2011-index.xml',
                    'https://www.news18.com/text-sitemap-2010-index.xml',
                    'https://www.news18.com/text-sitemap-2009-index.xml',

                    ]

    def parse(self, response):

        html = response.body
        article = NewsPlease.from_html(html)


        keywords = response.css('meta[name=news_keywords]::attr(content)').extract()
        subsection = response.css('meta[name=subsection]::attr(content)').extract()
        articleSection = response.css('meta[itemprop=articleSection]::attr(content)').extract()
        news_topics = response.css('div.tag a::text').extract()


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

