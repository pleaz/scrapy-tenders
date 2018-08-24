# -*- coding: utf-8 -*-
import scrapy


class TendersGovAuSpider(scrapy.Spider):
    name = 'tenders.gov.au'
    allowed_domains = ['tenders.gov.au']
    start_urls = [
     #   'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=sonSearchEvent&dateType=Publish+Date'
        'https://www.tenders.gov.au/?event=public.ATM.list'

    ]

    def parse(self, response):
        pages = response.xpath('//div[1][@class="list-desc"]/div[@class="list-desc-inner"]/a/@href').extract()
        for url in pages:
            yield scrapy.Request(response.urljoin(url), callback=self.parse_page)

        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

    def parse_page(self, response):
        yield {
            'atm_id': response.xpath(
                '//div[contains(.//span/text(), "ATM ID:")]/div[@class="list-desc-inner"]//text()'
            ).extract_first().strip(),
            'agency': response.xpath(
                '//div[contains(.//span/text(), "Agency:")]/div[@class="list-desc-inner"]//text()'
            ).extract_first().strip(),
            'publish_date': response.xpath(
                '//div[contains(.//span/text(), "Publish Date:")]/div[@class="list-desc-inner"]//text()'
            ).extract_first().strip(),
            'category': response.xpath(
                '//div[contains(.//span/text(), "Category:")]/div[@class="list-desc-inner"]//text()'
            ).extract_first().strip(),
            'period': response.xpath(
                '//div[contains(.//span/text(), "Close Date & Time:")]/div[@class="list-desc-inner"]//text()'
            ).extract_first().strip(),
            'type': response.xpath(
                '//div[contains(.//span/text(), "ATM Type:")]/div[@class="list-desc-inner"]//text()'
            ).extract_first().strip(),
            'description': response.xpath(
                '//div[contains(.//span/text(), "Description:")]/div[@class="list-desc-inner"]//text()'
            ).extract_first().strip(),
            'location': response.xpath(
                '//div[contains(.//span/text(), "Location:")]/div[@class="list-desc-inner"]//text()'
            ).extract_first().strip(),
            'title': response.xpath(
                '//div[@class="box boxY boxY1"]/p/text()'
            ).extract_first().strip()
        }

