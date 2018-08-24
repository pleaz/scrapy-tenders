# -*- coding: utf-8 -*-
import scrapy


class TestGovAuSpider(scrapy.Spider):
    name = 'test.gov.au'
    allowed_domains = ['tenders.gov.au']
    start_urls = [
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueTo=5000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=5000&valueTo=10000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=10000&valueTo=10500&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=10500&valueTo=11000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=11000&valueTo=11500&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=11500&valueTo=12000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=12000&valueTo=13000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=13000&valueTo=14000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=14000&valueTo=14500&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=14500&valueTo=15000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=15000&valueTo=15500&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=15500&valueTo=16000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=16000&valueTo=17000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=17000&valueTo=18000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=18000&valueTo=19000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=19000&valueTo=19500&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=19500&valueTo=20000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=20000&valueTo=21000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=21000&valueTo=22000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=22000&valueTo=23000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=23000&valueTo=24000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=24000&valueTo=25000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=25000&valueTo=26000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=26000&valueTo=27000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=27000&valueTo=28000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=28000&valueTo=29000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=29000&valueTo=30000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=30000&valueTo=32000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=32000&valueTo=34000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=34000&valueTo=36000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=36000&valueTo=38000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=38000&valueTo=40000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=40000&valueTo=43000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=43000&valueTo=46000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=46000&valueTo=49000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=49000&valueTo=50000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=50000&valueTo=52500&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=52500&valueTo=55000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=55000&valueTo=57500&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=57500&valueTo=60000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=60000&valueTo=65000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=65000&valueTo=70000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=70000&valueTo=75000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=75000&valueTo=77500&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=77500&valueTo=80000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=80000&valueTo=85000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=85000&valueTo=90000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=90000&valueTo=95000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=95000&valueTo=100000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=100000&valueTo=105000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=105000&valueTo=110000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=110000&valueTo=115000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=115000&valueTo=120000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=120000&valueTo=125000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=125000&valueTo=135000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=135000&valueTo=145000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=145000&valueTo=165000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=165000&valueTo=185000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=185000&valueTo=205000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=205000&valueTo=235000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=235000&valueTo=245000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=245000&valueTo=285000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=285000&valueTo=325000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=325000&valueTo=365000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=365000&valueTo=405000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=405000&valueTo=445000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=445000&valueTo=485000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=485000&valueTo=525000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=525000&valueTo=565000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=565000&valueTo=605000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=605000&valueTo=645000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=645000&valueTo=685000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=685000&valueTo=725000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=725000&valueTo=765000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=765000&valueTo=805000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=805000&valueTo=845000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=845000&valueTo=925000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=925000&valueTo=990000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=990000&valueTo=2000000&category=55',
        'https://www.tenders.gov.au/?event=public.advancedsearch.CNSONRedirect&type=cnSearchEvent&valueFrom=2000000&category=55'
    ]

    def parse(self, response):
        yield {
            'total': response.xpath(
                '//div[@class="col-sm-5 col-md-6 total-result"]/strong/text()'
            ).extract_first().strip()
        }

