# -*- coding: utf-8 -*-
import scrapy


class TendersSpider(scrapy.Spider):
    name = 'son_nsw'
    allowed_domains = ['tenders.nsw.gov.au']
    start_urls = [
    'https://tenders.nsw.gov.au/?event=public.advancedsearch.SONRedirect&invalidEventName=public.SON.search&type=SONEvent&agencyStatus=-1&submit=Search'
    ]

    def parse(self, response):
        pages = response.xpath('//div[@class="list-box"]//a[@class="list-item-title"]/@href').extract()
        for url in pages:
            yield scrapy.Request(response.urljoin(url), callback=self.parse_page)

        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

    @staticmethod
    def parse_page(response):

        name = response.xpath('//h1/text()').extract_first()
        sonid = response.xpath('//div[@id="SON-SB-ID"]/span[@class="sidebarBlock-content"]/text()').extract_first()
        agency = response.xpath('//div[@id="SON-SB-Agency"]/span[@class="sidebarBlock-content"]/text()').extract_first()
        published = response.xpath(
            '//div[@id="SON-SB-Published"]/span[@class="sidebarBlock-content"]/text()'
        ).extract_first()
        category = response.xpath(
            '//div[@id="SON-SB-Category"]/span[@class="sidebarBlock-content"]/text()[preceding-sibling::br]'
        ).extract_first()
        description = response.xpath(
            '//div[@id="SON-SB-ParticularsGoodsServices"]/div[@class="sidebarBlock-content"]//text()[normalize-space()]'
        ).extract_first()
        period = response.xpath(
            '//div[@id="SON-SB-StandingOfferDuration"]/span[@class="sidebarBlock-content"]/text()'
        ).extract_first()
        """
        suppliers = response.xpath(
            '//table[contains(.//th, "Supplier Name")]//td[contains(text(),"Business Name: ")]/text()'
        ).re(r'Business Name: (.*) ')
        abn = 
        """
        procurement_method = response.xpath(
            '//div[@id="SON-ProcurementMethod"]/div[@class="richtextblock-content"]//text()'
        ).extract_first()
        location = response.xpath('//div[@id="SON-TownCity"]//text()[preceding-sibling::strong]').extract_first()

        item = {}
        if name:
            item['name'] = name.strip()
        if sonid:
            item['sonid'] = sonid.strip()
        if agency:
            item['agency'] = agency.strip()
        if published:
            item['published'] = published.strip()
        if category:
            item['category'] = category.strip()
        if description:
            item['description'] = description.strip()
        if period:
            item['period'] = period.strip()
        if procurement_method:
            item['procurement_method'] = procurement_method.strip()
        if location:
            item['location'] = location.strip()

        yield item
