# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta
import datetime
import re

import scrapy


class VicTendersSpider(scrapy.Spider):
    name = 'vic_tenders'
    allowed_domains = ['www.tenders.vic.gov.au']

    def start_requests(self):

        result = []
        today = datetime.date(2017, 5, 1)
        current = datetime.date(2004, 12, 1)

        while current <= today:
            result.append(current)
            current += relativedelta(months=1)

        for i in result:
            if i == result[len(result) - 1]:
                yield scrapy.Request(
                    "https://www.tenders.vic.gov.au/tenders/tender/search/tender-search.do?"
                    "action=do-advanced-tender-search"
                    "&ageRestriction=0"
                    "&state=Any"
                    "&openingDateFromString=" + result[len(result) - 1].strftime("%d/%m/%Y"),
                    callback=self.parse
                )
            elif i == result[0]:
                yield scrapy.Request(
                    "https://www.tenders.vic.gov.au/tenders/tender/search/tender-search.do?"
                    "action=do-advanced-tender-search"
                    "&ageRestriction=0"
                    "&state=Any"
                    "&openingDateToString=" + result[0].strftime("%d/%m/%Y"),
                    callback=self.parse
                )
                yield scrapy.Request(
                    "https://www.tenders.vic.gov.au/tenders/tender/search/tender-search.do?"
                    "action=do-advanced-tender-search"
                    "&ageRestriction=0"
                    "&state=Any"
                    "&openingDateFromString=" + i.strftime("%d/%m/%Y") +
                    "&openingDateToString=" + (i + relativedelta(months=1)).strftime("%d/%m/%Y"),
                    callback=self.parse
                )
            else:
                yield scrapy.Request(
                    "https://www.tenders.vic.gov.au/tenders/tender/search/tender-search.do?"
                    "action=do-advanced-tender-search"
                    "&ageRestriction=0"
                    "&state=Any"
                    "&openingDateFromString=" + i.strftime("%d/%m/%Y") +
                    "&openingDateToString=" + (i + relativedelta(months=1)).strftime("%d/%m/%Y"),
                    callback=self.parse
                )

    def parse(self, response):
        pages = response.xpath('//tr[contains(./td/a/@id, "MSG")]')
        item = {}
        if pages:
            for page in pages:
                link_id = page.xpath('./td/a[1]/@href').re(r'id=([0-9]+)')[0]
                if link_id:
                    item['link_id'] = link_id.strip()
                tender_id = page.xpath('./td/b/text()').extract_first()
                if tender_id:
                    item['tender_id'] = tender_id.strip()
                status = page.xpath('./td/font/b/text()').extract_first()
                if status:
                    item['status'] = status.strip()
                tender_type = page.xpath('./td[2]/text()[normalize-space()]').extract_first()
                if tender_type:
                    item['type'] = tender_type.strip()
                title = page.xpath('./td/a/text()').extract_first()
                if title:
                    item['title'] = title.strip()
                issuer = page.xpath('./td/span/text()').re(r'^Issued by (.*)')[0]
                if issuer:
                    item['issuer'] = issuer.strip()
                unspsc = page.xpath('./td/span/span/text()').extract_first()
                if unspsc:
                    item['unspsc'] = unspsc.strip()
                closed = page.xpath('./td/span[contains(@class, "SUMMARY_CLOSINGDATE")]/text()').extract_first()
                if closed:
                    item['closed'] = closed.strip()
                opened = page.xpath('./td/span[contains(@class, "SUMMARY_OPENINGDATE")]/text()').extract_first()
                if opened:
                    item['opened'] = opened.strip()
                location = page.xpath(
                    './td/span[contains(@class, "SUMMARY_OPENINGDATE")]/text()[preceding-sibling::br]'
                ).extract_first()
                if location:
                    item['location'] = location.strip()

                yield item

        next_page = response.xpath('//span[contains(./u/text(), "Next")]/@onclick').extract_first()
        if next_page:
            next_page = next_page.replace('gotoPage(', '')
            next_page = re.sub(r', \'(|[-\\+0-9]+)\'(|,\'[-A-Za-z]+\')\);', '', next_page)
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
