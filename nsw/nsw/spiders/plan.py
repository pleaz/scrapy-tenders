# -*- coding: utf-8 -*-
import scrapy


class TendersSpider(scrapy.Spider):
    name = 'plans_nsw'
    allowed_domains = ['tenders.nsw.gov.au']
    start_urls = [
    'https://tenders.nsw.gov.au/?event=public.advancedsearch.APPRedirect&type=appEvent&rftType=proposed%2Cpublished%2Cclosed%2Carchived&agencyStatus=-1&submit=Search'
    ]

    def parse(self, response):
        for plan in response.xpath('//div[contains(@class, "list-box-inner")]'):
            yield {
                'name': plan.xpath('.//h2/a/text()').extract_first(),
                'agency': plan.xpath('.//div/text()[preceding-sibling::strong[contains(text(),"Agency")][2]]').extract_first().strip(),
                'agency_ref': plan.xpath('.//div/text()[preceding-sibling::strong[contains(text(),"Agency Reference")]]').extract_first().strip(),
                'category': plan.xpath('.//div/text()[preceding-sibling::strong[contains(text(),"Category")]]').extract_first().strip(),
                'date': plan.xpath('.//div/text()[preceding-sibling::strong[contains(text(),"Estimated Date of Approach to Market")]]').extract_first().strip(),
                'multi_agency': plan.xpath('.//div/text()[preceding-sibling::strong[contains(text(),"Multi Agency Access")]]').extract_first().strip(),
                'status': plan.xpath('.//div/text()[preceding-sibling::strong[contains(text(),"Status")]]').extract_first().strip(),
                'contact': plan.xpath('.//div/text()[preceding-sibling::strong[contains(text(),"Contact")]]').extract_first().strip(),
                'last_updated': plan.xpath('.//p/text()[preceding-sibling::strong[contains(text(),"Last Updated")]]').extract_first().strip()
            }

        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
