# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta
import datetime
import re

import scrapy


class VicContractsSpider(scrapy.Spider):
    name = 'vic_contracts'
    allowed_domains = ['www.tenders.vic.gov.au']
    # start_urls = ['http://www.tenders.vic.gov.au/']

    def start_requests(self):

        result = []
        today = datetime.date(2017, 3, 1)
        current = datetime.date(2002, 8, 1)

        while current <= today:
            result.append(current)
            current += relativedelta(months=1)

        for i in result:
            if i == result[len(result) - 1]:
                yield scrapy.Request(
                    "https://www.tenders.vic.gov.au/tenders/contract/list.do?action=contract-search-submit"
                    "&startingDateFromString=" + result[len(result) - 1].strftime("%d/%m/%Y"),
                    callback=self.parse
                )
            elif i == result[0]:
                yield scrapy.Request(
                    "https://www.tenders.vic.gov.au/tenders/contract/list.do?action=contract-search-submit"
                    "&startingDateToString=" + result[0].strftime("%d/%m/%Y"),
                    callback=self.parse
                )
                yield scrapy.Request(
                    "https://www.tenders.vic.gov.au/tenders/contract/list.do?action=contract-search-submit"
                    "&startingDateFromString=" + i.strftime("%d/%m/%Y") +
                    "&startingDateToString=" + (i + relativedelta(months=1)).strftime("%d/%m/%Y"),
                    callback=self.parse
                )
            else:
                yield scrapy.Request(
                    "https://www.tenders.vic.gov.au/tenders/contract/list.do?action=contract-search-submit"
                    "&startingDateFromString=" + i.strftime("%d/%m/%Y") +
                    "&startingDateToString=" + (i + relativedelta(months=1)).strftime("%d/%m/%Y"),
                    callback=self.parse
                )

    def parse(self, response):
        pages = response.xpath('//a[re:test(@id, "^MSG[0-9]+$")]/@href').extract()
        if pages:
            for url in pages:
                yield scrapy.Request(response.urljoin(url), callback=self.parse_page)

        next_page = response.xpath('//span[contains(./u/text(), "Next")]/@onclick').extract_first()
        if next_page:
            next_page = next_page.replace('gotoPage(', '')
            next_page = re.sub(r', [-\\+0-9]+\);', '', next_page)
            sub_next = eval(next_page)

            pager = '&pageNum='
            new_url = response.request.url
            if new_url.find(pager) != -1:
                gen_url = re.sub(pager + '[0-9]+', pager + str(sub_next), new_url)
                yield scrapy.Request(
                    response.urljoin(gen_url),
                    callback=self.parse
                )
            else:
                yield scrapy.Request(
                    response.urljoin(new_url + pager + str(sub_next)),
                    callback=self.parse
                )

    @staticmethod
    def parse_page(response):

        item = {}
        cnid = response.xpath('//td[contains(./span/text(), "Contract Number:")]/following-sibling::td/text()').extract_first()
        contact_person = response.xpath('//td[contains(./span/text(), "Contact Person:")]/following-sibling::td/text()').extract_first()
        contact_number = response.xpath('//td[contains(./span/text(), "Contact Number:")]/following-sibling::td/text()').extract_first()
        published = response.xpath('//td[contains(./span/text(), "Start Date:")]/following-sibling::td/text()').extract_first()
        closes = response.xpath('//td[contains(./span/text(), "Expiry Date:")]/following-sibling::td/text()').extract_first()
        category = response.xpath('//td[contains(./span/text(), "Type of Contract:")]/following-sibling::td/text()').extract_first()
        value = response.xpath('//td[contains(./span/text(), "Total Value of the Contract:")]/following-sibling::td/text()').extract_first()
        title = response.xpath('//td[contains(./span/text(), "Title:")]/following-sibling::td/text()').extract_first()
        public_body = response.xpath('//td[contains(./span/text(), "Public Body:")]/following-sibling::td/text()').extract_first()
        status = response.xpath('//td[contains(./span/text(), "Status:")]/following-sibling::td/text()').extract_first()
        unspsc = response.xpath('//td[contains(./span/text(), "UNSPSC")]/following-sibling::td/span/text()').extract_first()
        description = response.xpath('//div[contains(./h2, "Description")]/following-sibling::table/tr/td[2]').extract_first()

        if cnid:
            item['cnid'] = cnid.strip()
        if contact_person:
            item['contact_person'] = contact_person.strip()
        if contact_number:
            item['contact_number'] = contact_number.strip()
        if published:
            item['published'] = published.strip()
        if closes:
            item['closes'] = closes.strip()
        if category:
            item['category'] = category.strip()
        if value:
            item['value'] = value.strip()
        if status:
            item['status'] = status.strip()
        if unspsc:
            item['unspsc'] = unspsc.strip()
        if title:
            item['title'] = title.strip()
        if public_body:
            item['public_body'] = public_body.strip()
        if description:
            item['description'] = description.strip()

        yield item
