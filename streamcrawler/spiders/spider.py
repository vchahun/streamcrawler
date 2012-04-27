from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy import log
from streamcrawler.items import StreamcrawlerItem

from itertools import count
import time

class StreamSpider(CrawlSpider):
    name = 'streamspider'

    def start_requests(self):
        self.block = False
        for i in count():
            while self.block:
                time.sleep(5)
            log.msg('Generated item')
            yield Request('http://www.google.com/?q=%d' % i)
            self.block = True

    def parse(self, response):
        log.msg('Retrieved item %s' % response.url)
        self.block = False
