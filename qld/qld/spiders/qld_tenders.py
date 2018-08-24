# -*- coding: utf-8 -*-
import scrapy
import re


class QldTendersSpider(scrapy.Spider):
    name = 'qld_tenders'
    allowed_domains = ['www.hpw.qld.gov.au']
    # start_urls = ['https://www.hpw.qld.gov.au/qtenders/tender/search/tender-search.do?action=advanced-tender-search-open-tender&orderBy=closeDate']
    # start_urls = ['https://www.hpw.qld.gov.au/qtenders/tender/search/tender-search.do?action=advanced-tender-search-closed-tender&orderBy=closeDate']
    start_urls = ['https://www.hpw.qld.gov.au/qtenders/tender/search/tender-search.do?action=advanced-tender-search-awarded-tender&orderBy=closeDate']

    def parse(self, response):
        pages = response.xpath('//tr/td/a[@id="MSG"]/@href').extract()
        for url in pages:
            yield scrapy.Request(response.urljoin(url), callback=self.parse_page)

        for x in range(2, 7):  # 5 # 12
            pager = '&pageNum='
            new_url = response.request.url
            if new_url.find(pager) != -1:
                gen_url = re.sub(pager + '[0-9]+', pager + str(x), new_url)
                yield scrapy.Request(
                    response.urljoin(gen_url),
                    callback=self.parse
                )
            else:
                yield scrapy.Request(
                    response.urljoin(new_url + pager + str(x)),
                    callback=self.parse
                )

    @staticmethod
    def parse_page(response):

        item = {}
        status = response.xpath(
            '//td[contains(./span/text(), "Status:")]/following-sibling::td/text()'
        ).extract_first()
        category = response.xpath(
            '//td[contains(./span/text(), "Mega Category:")]/following-sibling::td/text()'
        ).extract_first()
        number = response.xpath(
            '//td[contains(./span/text(), "Number:")]/following-sibling::td/text()'
        ).extract_first()
        released = response.xpath(
            '//td[contains(./span/text(), "Released:")]/following-sibling::td/text()'
        ).extract_first()
        closes = response.xpath(
            '//td[contains(./span/text(), "Clos")]/following-sibling::td/text()'
        ).extract_first()
        awarded = response.xpath(
            '//td[contains(./span/text(), "Awarded:")]/following-sibling::td/text()'
        ).extract_first()
        unspsc = response.xpath(
            '//td[contains(./span/text(), "UNSPSC:")]/following-sibling::td/text()'
        ).extract_first()
        unspsc2 = response.xpath(
            '//td[contains(./span/text(), "UNSPSC 2:")]/following-sibling::td/text()'
        ).extract_first()
        regions = response.xpath(
            '//td[contains(./span/text(), "Region/s:")]/following-sibling::td/text()'
        ).extract_first()
        title = response.xpath(
            '//td/span[@class="TITLE"]/text()[normalize-space()]'
        ).extract_first()
        issued = response.xpath(
            '//td/span[contains(./text(), "Issued by ")]/text()'
        ).extract_first()

        if status:
            item['status'] = status.strip()
        if category:
            item['category'] = category.strip()
        if number:
            item['number'] = number.strip()
        if released:
            item['released'] = released.strip()
        if closes:
            item['closes'] = closes.strip()
        if awarded:
            item['awarded'] = awarded.strip()
        if unspsc:
            item['unspsc'] = unspsc.strip()
        if unspsc2:
            item['unspsc2'] = unspsc2.strip()
        if title:
            item['title'] = title.strip()
        if issued:
            item['issued'] = issued.strip()
        if regions:
            item['regions'] = regions.strip()

        yield item
