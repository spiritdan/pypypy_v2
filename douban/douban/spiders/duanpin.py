# -*- coding: utf-8 -*-
import scrapy
import bs4
from ..items import DoubanItem
import re

class DuanpinSpider(scrapy.Spider):
    name = 'duanpin'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250?start=0','https://book.douban.com/top250?start=25']

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        print(bs.text)
        div_list = bs.find_all('div', class_="pl2")
        print(div_list)
        for div in div_list:
            link = div.find('a')['href']
            print(link)
            yield scrapy.Request(link, callback=self.parse_book)
        # 用yield语句把构造好的request对象传递给引擎。用scrapy.Request构造request对象。callback参数设置调用parsejob方法。

    def parse_book(self, response):
        # 定义新的处理response的方法parse_job（方法的名字可以自己起）
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        # 用BeautifulSoup解析response(公司招聘信息的网页源代码)
        shot_comment_url = bs.find('div', class_="mod-hd").find('span', class_="pl").find('a')['href']
        print(shot_comment_url)
        yield scrapy.Request(shot_comment_url, callback=self.parse_comment)



    def parse_comment(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')

        comments = bs.find('span', id='total-comments').text
        num = int(re.findall('\d+', comments)[0])
        if num % 20 == 0:
            page_num = int(num / 20)
        else:
            page_num = int(num / 20) + 1
        for i in range(1, page_num + 1):
            final_url = 'https://book.douban.com/subject/1770782/comments/hot?p={0}'.format(i)
            print(final_url)
            yield scrapy.Request(final_url, callback=self.parse_comment_details)



    def parse_comment_details(self, response):
        item=DoubanItem()

        bs = bs4.BeautifulSoup(response.text, 'html.parser')

        list_comments = bs.find_all('li', class_='comment-item')
        item['book'] =bs.find('div',id='content').text.strip()
        for comment in list_comments:

            item['user']=comment.find('span', class_='comment-info').find('a').text.strip()
            date_list = comment.find('span', class_='comment-info').find_all('span')
            if len(date_list) > 1:
                item['date'] = date_list[1].text
            else:
                item['date'] = date_list[0].text
            item['content'] = comment.find('p',class_='comment-content').text.strip()
            print(item)
        yield item