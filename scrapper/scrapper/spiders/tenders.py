# -*- coding: utf-8 -*-
import scrapy


class TendersSpider(scrapy.Spider):
    name = 'tenders'
    allowed_domains = ['tenders.gov.au']
    start_urls = [
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueTo=5000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=5000&valueTo=10000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=10000&valueTo=12000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=12000&valueTo=12500&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=12500&valueTo=15000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=15000&valueTo=17500&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=17500&valueTo=20000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=20000&valueTo=22500&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=22500&valueTo=25000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=25000&valueTo=30000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=30000&valueTo=35000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=35000&valueTo=40000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=40000&valueTo=45000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=45000&valueTo=50000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=50000&valueTo=55000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=55000&valueTo=60000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=60000&valueTo=65000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=65000&valueTo=70000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=70000&valueTo=75000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=75000&valueTo=80000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=80000&valueTo=85000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=85000&valueTo=90000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=90000&valueTo=95000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=95000&valueTo=100000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=100000&valueTo=105000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=105000&valueTo=110000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=110000&valueTo=115000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=115000&valueTo=120000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=120000&valueTo=125000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=125000&valueTo=165000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=165000&valueTo=205000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=205000&valueTo=245000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=245000&valueTo=285000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=285000&valueTo=325000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=325000&valueTo=365000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=365000&valueTo=405000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=405000&valueTo=445000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=445000&valueTo=485000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=485000&valueTo=525000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=525000&valueTo=565000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=565000&valueTo=605000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=605000&valueTo=645000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=645000&valueTo=685000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=685000&valueTo=725000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=725000&valueTo=765000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=765000&valueTo=805000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=805000&valueTo=845000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=845000&valueTo=925000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=925000&valueTo=990000&category=86',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=990000&category=86'
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
            'cnid': response.xpath(
                '//div[contains(.//span/text(), "CN ID:")]/div[@class="list-desc-inner"]//text()'
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
            'contract_period': response.xpath(
                '//div[contains(.//span/text(), "Contract Period:")]/div[@class="list-desc-inner"]//text()'
            ).extract_first().strip(),
            'contract_value': response.xpath(
                '//div[contains(.//span/text(), "Contract Value")]/div[@class="list-desc-inner"]//text()'
            ).extract_first().strip(),
            'description': response.xpath(
                '//div[contains(.//span/text(), "Description:")]/div[@class="list-desc-inner"]//text()'
            ).extract_first().strip(),
            'procurement_method': response.xpath(
                '//div[contains(.//span/text(), "Procurement Method:")]/div[@class="list-desc-inner"]//text()'
            ).extract_first().strip(),
            'vendor': response.xpath(
                '//div[contains(.//span/text(), "Name:")]/div[@class="list-desc-inner"]//text()'
            ).extract_first().strip(),
            'vendor_abn': response.xpath(
                '//div[contains(.//span/text(), "ABN:")]/div[@class="list-desc-inner"]//text()'
            ).extract_first().strip(),
        }