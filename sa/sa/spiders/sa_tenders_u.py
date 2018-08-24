# -*- coding: utf-8 -*-
import scrapy
from sa.items import SaItem


class SaTendersSpider(scrapy.Spider):
    name = 'sa_tenders_u'
    allowed_domains = ['www.tenders.sa.gov.au']
    start_urls = ['https://www.tenders.sa.gov.au/tenders/tender/search/tender-search.do?action=do-advanced-tender-search&inputlist=hasETB&state=Any&type=Any&unspsc=-1&issuingBusinessId=-1&dateOpeningIndex=1&dateClosingIndex=1&groupBy=None']

    def parse(self, response):
        for block in response.xpath('//tr[contains(.//a/@id, "MSG")]'):
            item = SaItem()
            item_id = block.xpath('.//td/a/@href').re(r'\?id=([0-9]+)&')
            item_close = block.xpath('.//td//span[@class="SUMMARY_CLOSINGDATE"]/text()').extract_first()
            if item_id:
                item['item_id'] = item_id[0]
                if item_close:
                    item['closes'] = item_close.strip()
                    yield item
