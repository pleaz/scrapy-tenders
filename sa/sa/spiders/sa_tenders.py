# -*- coding: utf-8 -*-
import scrapy
import re


class SaTendersSpider(scrapy.Spider):
    name = 'sa_tenders'
    allowed_domains = ['www.tenders.sa.gov.au']
    start_urls = ['https://www.tenders.sa.gov.au/tenders/tender/search/tender-search.do?action=do-advanced-tender-search&inputlist=hasETB&state=Any&type=Any&unspsc=-1&issuingBusinessId=-1&dateOpeningIndex=1&dateClosingIndex=1&groupBy=None']

    def parse(self, response):
        pages = response.xpath('//a[@id="MSG"]/@href').extract()
        for url in pages:
            yield scrapy.Request(response.urljoin(url), callback=self.parse_page)

    @staticmethod
    def parse_page(response):

        tender_id = re.findall(r'id=([0-9]+)&', response.url)
        name = response.xpath('//span[@class="TITLE"]/span/text()').extract_first()
        tender_code = response.xpath('//td[preceding-sibling::td[contains(.//text(), "Tender Code:")]]/text()').extract_first()
        category = response.xpath('//td[preceding-sibling::td[contains(.//text(), "Category:")]]/text()').extract_first()
        contract_number = response.xpath('//td[preceding-sibling::td[contains(.//text(), "Contract Number:")]]/text()').extract_first()
        tender_state = response.xpath('//td[preceding-sibling::td[contains(.//text(), "Tender State:")]]/text()').extract_first()
        description = response.xpath('//tr[preceding-sibling::tr/th[contains(./h2/text(), "Description")]]/td[1]//text()[normalize-space()]').extract_first()
        issuer = response.xpath('//span[@class="TITLE"]/span/text()').re(r'Issued by (.*)')
        contact_name = response.xpath('//td[preceding-sibling::td[contains(./i/@aria-label, "Contact")]]//text()').extract_first()
        contact_phone = response.xpath('//td[preceding-sibling::td[contains(./i/@aria-label, "Phone")]]//text()').extract_first()

        item = {}
        if name:
            item['name'] = name.strip()
        if tender_id:
            item['tender_id'] = tender_id[0]
        if tender_code:
            item['tender_code'] = tender_code.strip()
        if contract_number:
            item['contract_number'] = contract_number.strip()
        if tender_state:
            item['tender_state'] = tender_state.strip()
        if description:
            item['description'] = description.strip()
        if issuer:
            item['issuer'] = issuer[0]
        if category:
            item['category'] = category.strip()
        if contact_name:
            item['contact_name'] = contact_name.strip()
        if contact_phone:
            item['contact_phone'] = contact_phone.strip()

        yield item

