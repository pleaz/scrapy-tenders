# -*- coding: utf-8 -*-
import scrapy
import re


class SaTendersSpider(scrapy.Spider):
    name = 'sa_contracts'
    allowed_domains = ['www.tenders.sa.gov.au']
    start_urls = [
        'https://www.tenders.sa.gov.au/tenders/contract/list.do?action=contract-search-submit&issuingBusinessId=-1'
    ]

    def parse(self, response):
        pages = response.xpath('//a[@id="MSG"]/@href').extract()
        for url in pages:
            yield scrapy.Request(response.urljoin(url), callback=self.parse_page)

    @staticmethod
    def parse_page(response):

        contract_id = re.findall(r'id=([0-9]+)', response.url)
        number = response.xpath('//td[preceding-sibling::td[contains(./span/label/text(), "Reference #")]]//text()').extract_first()
        assoc_tender = response.xpath('//td[preceding-sibling::td[contains(./span/label/text(), "Associated with Tender")]]//text()').extract_first()
        name = response.xpath('//td[preceding-sibling::td[contains(./span/label/text(), "Name of Public Authority")]]//text()').extract_first()
        title = response.xpath('//td[preceding-sibling::td[contains(./span/label/text(), "Title")]]//text()').extract_first()
        description = response.xpath('//td[preceding-sibling::td[contains(./span/label/text(), "Good or Services Acquired")]]').extract_first()
        procurement = response.xpath('//td[preceding-sibling::td[contains(./span/label/text(), "Procurement Process")]]//text()').extract_first()
        value = response.xpath('//td[preceding-sibling::td[contains(./span/label/text(), "Total inc GST")]]//text()').extract_first()
        execution_date = response.xpath('//td[preceding-sibling::td[contains(./span/label/text(), "Execution Date")]]//text()').extract_first()
        starting_date = response.xpath('//td[preceding-sibling::td[contains(./span/label/text(), "Starting Date")]]//text()').extract_first()
        completion_date = response.xpath('//td[preceding-sibling::td[contains(./span/label/text(), "Completion Date")]]//text()').extract_first()
        info_officer = response.xpath('//td[preceding-sibling::td[contains(./span/label/text(), "Freedom of Information Officer")]]//text()').extract_first()
        phone = response.xpath('//td[preceding-sibling::td[contains(./span/label/text(), "Phone")]]//text()').extract_first()
        email = response.xpath('//td[preceding-sibling::td[contains(./span/label/text(), "E-Mail")]]//a/text()').extract_first()
        agency = response.xpath('//td[preceding-sibling::td[contains(./span/label/text(), "Agency Unit")]]//text()').extract_first()

        vendor_org = response.xpath('//table[@summary="displays contractors"]//td[2]//text()').extract_first()
        vendor_address = response.xpath('//table[@summary="displays contractors"]//td[2]//text()[preceding-sibling::br]').extract_first()
        vendor_name = response.xpath(
            '//table[@summary="displays contractors"]//td//text()[preceding-sibling::i[contains(@class, "fa-users")]][normalize-space()]').extract_first()
        vendor_abn = response.xpath(
            '//table[@summary="displays contractors"]//td//text()[preceding-sibling::i[contains(@class, "fa-phone")]][normalize-space()]').extract_first()

        item = {}
        if contract_id:
            item['contract_id'] = contract_id[0]
        if number:
            item['number'] = number.strip()
        if assoc_tender:
            item['assoc_tender'] = assoc_tender.strip()
        if name:
            item['name'] = name.strip()
        if title:
            item['title'] = title.strip()
        if description:
            item['description'] = description.strip()
        if procurement:
            item['procurement'] = procurement.strip()
        if value:
            item['value'] = value.strip()
        if execution_date:
            item['execution_date'] = execution_date.strip()
        if starting_date:
            item['starting_date'] = starting_date.strip()
        if completion_date:
            item['completion_date'] = completion_date.strip()
        if info_officer:
            item['info_officer'] = info_officer.strip()
        if phone:
            item['phone'] = phone.strip()
        if email:
            item['email'] = email.strip()
        if agency:
            item['agency'] = agency.strip()
        if vendor_org:
            item['vendor_org'] = vendor_org.strip()
        if vendor_address:
            item['vendor_address'] = vendor_address.strip()
        if vendor_name:
            item['vendor_name'] = vendor_name.strip()
        if vendor_abn:
            item['vendor_abn'] = vendor_abn.strip()

        yield item
