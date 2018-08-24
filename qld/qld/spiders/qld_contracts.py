# -*- coding: utf-8 -*-
import scrapy
import re


class QldContractsSpider(scrapy.Spider):
    name = 'qld_contracts'
    allowed_domains = ['www.hpw.qld.gov.au']
    start_urls = ['https://www.hpw.qld.gov.au/qtenders/contract/list.do?action=gotoPage&isSearch=true&regionId=-1']

    def parse(self, response):
        pages = response.xpath('//tr/td[1]/a[@id="MSG"]/@href').extract()
        for url in pages:
            yield scrapy.Request(response.urljoin(url), callback=self.parse_page)

        next_page = response.xpath('//table[@class="paging"]//td/a[contains(text(), ">")]/@href').extract_first()
        if next_page:
            pager = '&pageNum='
            new_url = response.request.url
            if new_url.find(pager) != -1:
                sub_next = re.search(r'pageNum=([0-9]+)', new_url)
                sub = sub_next.group(1)
                sub = int(sub) + 1
                gen_url = re.sub(pager + '[0-9]+', pager + str(sub), new_url)
                yield scrapy.Request(
                    response.urljoin(gen_url),
                    callback=self.parse
                )
            else:
                yield scrapy.Request(
                    response.urljoin(new_url + pager + '2'),
                    callback=self.parse
                )

    @staticmethod
    def parse_page(response):

        item = {}
        agency = response.xpath(
            '//td[contains(./span/label/text(), "Agency")]/following-sibling::td/text()'
        ).extract_first()
        address = response.xpath(
            '//td[contains(./span/label/text(), "Address")]/following-sibling::td/text()'
        ).extract_first()
        cn_id = response.xpath(
            '//td[contains(./span/label/text(), "Reference number")]/following-sibling::td/text()'
        ).extract_first()
        cn_type = response.xpath(
            '//td[contains(./span/label/text(), "Type of Work")]/following-sibling::td/text()'
        ).extract_first()
        title = response.xpath(
            '//td[contains(./span/label/text(), "Title")]/following-sibling::td/text()'
        ).extract_first()
        description = response.xpath(
            '//td[contains(./span/label/text(), "Description")]/following-sibling::td/text()'
        ).extract_first()
        closes = response.xpath(
            '//td[contains(./span/label/text(), "Closing Date")]/following-sibling::td/text()'
        ).extract_first()
        unspsc = response.xpath(
            '//td[contains(./span/label/text(), "UNSPSC 1")]/following-sibling::td/text()'
        ).extract_first()
        method = response.xpath(
            '//td[contains(./span/label/text(), "Procurement Method")]/following-sibling::td/text()'
        ).extract_first()
        period = response.xpath(
            '//td[contains(./span/label/text(), "Period Contract")]/following-sibling::td/text()'
        ).extract_first()
        value = response.xpath(
            '//td[contains(./span/label/text(), "Total Value of the Contract")]/following-sibling::td/text()'
        ).extract_first()
        regions = response.xpath(
            '//td[contains(./span/label/text(), "Region/s")]/following-sibling::td/text()'
        ).extract_first()
        award_date = response.xpath(
            '//td[contains(./span/label/text(), "Award Date")]/following-sibling::td/text()'
        ).extract_first()
        final_date = response.xpath(
            '//td[contains(./span/label/text(), "Final Expiry Date")]/following-sibling::td/text()'
        ).extract_first()
        comments = response.xpath(
            '//td[contains(./span/label/text(), "Comments")]/following-sibling::td/text()'
        ).extract_first()
        submissions = response.xpath(
            '//td[contains(./span/label/text(), "Number of Submissions")]/following-sibling::td/text()'
        ).extract_first()
        contact = response.xpath(
            '//td[contains(./span/label/text(), "Contact")]/following-sibling::td/text()'
        ).extract_first()
        contractor = response.xpath(
            '//table[@summary="displays contractors"]//td[contains(./span/label/text(), "1)")]/following-sibling::td/text()'
        ).extract_first()

        if agency:
            item['agency'] = agency.strip()
        if address:
            item['address'] = address.strip()
        if cn_id:
            item['cnid'] = cn_id.strip()
        if cn_type:
            item['type'] = cn_type.strip()
        if title:
            item['title'] = title.strip()
        if description:
            item['description'] = description.strip()
        if closes:
            item['closes'] = closes.strip()
        if unspsc:
            item['unspsc'] = unspsc.strip()
        if method:
            item['method'] = method.strip()
        if period:
            item['period'] = period.strip()
        if value:
            item['value'] = value.strip()
        if regions:
            item['regions'] = regions.strip()
        if award_date:
            item['award_date'] = award_date.strip()
        if final_date:
            item['final_date'] = final_date.strip()
        if comments:
            item['comments'] = comments.strip()
        if submissions:
            item['submissions'] = submissions.strip()
        if contact:
            item['contact'] = contact.strip()
        if contractor:
            item['contractor'] = contractor.strip()

        yield item
