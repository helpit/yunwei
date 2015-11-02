# -*- coding:utf-8 -*-
__author__ = 'Kiun'
import scrapy
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader, Identity
from sys import argv
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from scrapy import log
log.msg("This is a warning", level=log.WARNING)
class NovelSpider(scrapy.Spider):
    name = "novel"
    allowed_domains = ["blah.me"]
    start_urls = [
        "http://blah.me/"
    ]
 
    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath("//div[@class='ok-book-item']")
        i = -1
 
        for site in sites:
            i += 1
            author = site.xpath("//div[@class='ok-book-author']/text()").extract()
            link = site.xpath("//a[@data-book-type='epub']/@href").extract()
            title =site.xpath("//a[@data-book-type='epub']/@data-book-title").extract()
            with open('/caonima.txt','a') as f:
                f.write(title[i].strip()+':http://blah.me'+link[i]+'\n')
            j = -1
            for l in link:
                j += 1
 
                url = 'http://blah.me'+ l
                filename = title[j]+'.epub'
                with open(filename, 'wb') as handle:
                    response = requests.get(url,stream=True)
                    if not response.ok:
                        # Something went wrong
                        print 'failed：%s' % (title[j]+':'+url)
                    for block in response.iter_content(1024):
                        if not block:
                            break
 
                        handle.write(block)
                    print '%s  finished' % (title[j])
        for link in range(2,100):
            request = scrapy.Request("http://blah.me/?p="+str(link), callback=self.parse)
            yield request
