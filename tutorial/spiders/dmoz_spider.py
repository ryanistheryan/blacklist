import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'blacklist'
    #allowed_domains = ['example.com']
    start_urls = ['https://www.google.com/search?q=blacklist+malware']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('blacklist', ), deny=('whitelist', ))),
		#Rule(LinkExtractor(allow=('blacklist', )), callback='parse_item'),
    )

    #def parse_item(self, response):
        #SearchItem = scrapy.Item()
        #SearchItem['link'] = response.xpath('//h3/a/@href').extract()
        #yield SearchItem 
