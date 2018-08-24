# -*- coding: utf-8 -*-
import scrapy


class TendersSpider(scrapy.Spider):
    name = 'contract_nsw'
    allowed_domains = ['tenders.nsw.gov.au']
    start_urls = [
    'https://tenders.nsw.gov.au/?keywordtypesearch=AllWord&event=public%2Eadvancedsearch%2EcnStep2&orderBy=Publish%20Date%20-%20Descending&type=cnEvent&rfttype=proposed%2Cpublished%2Cclosed%2Carchived&agencyStatus=0&numagencystatus=0&multype=archived%2Cclosed%2Cpublished'
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
        contractor = response.xpath('//div[@id="CN-Details"]//text()[preceding-sibling::strong[contains(text(),"Contractor Name")]]').extract_first()
        location = response.xpath('//div[@id="CN-Details"]//text()[preceding-sibling::strong[contains(text(),"Town/City")]]').extract_first()
        abn = response.xpath('//div[@id="CN-Details"]//text()[preceding-sibling::strong[contains(text(),"ABN")]]').extract_first()
        contract_id = response.xpath('//div[@id="CN-SB-ID"]/span[@class="sidebarBlock-content"]/text()').extract_first()
        agency = response.xpath('//div[@id="CN-SB-Agency"]/span[@class="sidebarBlock-content"]/text()').extract_first()
        published = response.xpath('//div[@id="CN-SB-PublishDate"]/span[@class="sidebarBlock-content"]/text()').extract_first()
        category = response.xpath('//div[@id="CN-SB-Category"]/span[@class="sidebarBlock-content"]/text()[preceding-sibling::br]').extract_first()
        description = response.xpath('//div[@id="CN-SB-ParticularsGoodsServices"]/div[@class="sidebarBlock-content"]//text()').extract_first()
        period = response.xpath('//div[@id="CN-SB-ContractDuration"]/span[@class="sidebarBlock-content"]/text()').extract_first()
        method = response.xpath('//div[@id="CN-MethodOfTendering"]/div[@class="richtextblock-content"]/p//text()').extract_first()
        value = response.xpath('//div[@id="CN-ContractValue"]/div[@class="richtextblock-content"]/p//text()').extract_first()

        item = {}
        if name:
            item['name'] = name.strip()
        if contract_id:
            item['contract_id'] = contract_id.strip()
        if contractor:
            item['contractor'] = contractor.strip()
        if abn:
            item['abn'] = abn.strip()
        if value:
            item['value'] = value.strip()
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
        if method:
            item['method'] = method.strip()
        if location:
            item['location'] = location.strip()

        yield item
