# -*- coding: utf-8 -*-
import scrapy


class TendersSpider(scrapy.Spider):
    name = 'tenders_nsw'
    allowed_domains = ['tenders.nsw.gov.au']
    start_urls = [
    'https://tenders.nsw.gov.au/?event=public.advancedsearch.rftStep2&type=rftEvent&rftType=proposed%2Cpublished%2Cclosed%2Carchived&agencyStatus=0&departmentUUID=B74FBC6B-F1D5-FD70-8001FAB1ECC4C391'
    ]

    def parse(self, response):
        for tender in response.xpath('//div[contains(@class, "list-box-inner")]'):
            name = tender.xpath('.//h2/a/text()').extract_first()
            rft_id = tender.xpath('.//div//text()[preceding-sibling::strong[contains(text(),"ID")]]').extract_first()
            rft_type = tender.xpath('.//div//text()[preceding-sibling::strong[contains(text(),"RFT Type")]]').extract_first()
            published = tender.xpath('.//div//text()[preceding-sibling::strong[contains(text(),"Published")]]').extract_first()
            issue_date = tender.xpath('.//div//text()[preceding-sibling::strong[contains(text(),"Expected Issue Date")]]').extract_first()
            closes = tender.xpath('.//div//text()[preceding-sibling::strong[contains(text(),"Closes")]]').extract_first()
            category = tender.xpath('.//div//text()[preceding-sibling::strong[contains(text(),"Category")]][3]').extract_first()
            agency = tender.xpath('.//div//text()[preceding-sibling::strong[contains(text(),"Agency")]]').extract_first()
            last_updated = tender.xpath('.//p//text()[preceding-sibling::strong[contains(text(),"Last Updated")]]').extract_first()
            item = {}
            if name:
                item['name'] = name.strip()
            if rft_id:
                item['rft_id'] = rft_id.strip()
            if rft_type:
                item['rft_type'] = rft_type.strip()
            if published:
                item['published'] = published.strip()
            if issue_date:
                item['issue_date'] = issue_date.strip()
            if closes:
                item['closes'] = closes.strip()
            if category:
                item['category'] = category.strip()
            if agency:
                item['agency'] = agency.strip()
            if last_updated:
                item['last_updated'] = last_updated.strip()
            yield item

        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
