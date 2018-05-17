# -*- coding: utf-8 -*-
import scrapy


class Ti8trackerSpider(scrapy.Spider):
    name = 'ti8tracker'
    allowed_domains = ['www.dota2.com/international/battlepass/']
    start_urls = ['https://www.dota2.com/international/battlepass//']

    def parse(self, response):
        prizepool = response.css(".PrizePool::text").extract_first() #'$9,251,067'
#        print(prizepool)
        prize_num = prizepool.replace(',','')[1:]
#        print(prize_num)
        pass
