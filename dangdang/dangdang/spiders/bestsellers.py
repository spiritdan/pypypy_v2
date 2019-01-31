# -*- coding: utf-8 -*-
import scrapy
import bs4
from ..items import DangdangItem


class BestsellersSpider(scrapy.Spider):
    name = 'bestseller'
    allowed_domains = ['http://bang.dangdang.com']
    start_urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-{0}'.format(i)for i in range (1,4)]

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        book_list=bs.select('.bang_list li')
        for book in book_list:
            item=DangdangItem()
            item['num'] = book.find('div',class_='list_num').text.strip()
            item['name'] = book.find('div',class_='name').text.strip()
            #item['star'] = book.find('div',class_='star').text.strip()
            '''
            publisher_infos=book.find_all('div',class_='publisher_info')
            publisher_info=[]
            for i in publisher_infos:
                publisher_info.append(i.text.strip())
            item['publisher_info'] = '\n'.join(publisher_info)
            '''
            item['price'] = book.find('div',class_='price').find('span',class_='price_n').text.strip()
            yield item
