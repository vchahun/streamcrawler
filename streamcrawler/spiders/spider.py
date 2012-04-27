from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy import log
from streamcrawler.items import StreamcrawlerItem

from itertools import count
import time

class StreamSpider(CrawlSpider):
    name = 'streamspider'

    def start_requests(self):
        for i in count():
            log.msg('Generated item')
            yield Request('http://www.example.com/?q=%d' % i)
            time.sleep(5)

    def parse_item(self, response):
        log.msg('Retrieved item %s' % response.url)
