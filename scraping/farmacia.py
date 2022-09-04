from tkinter.tix import Select
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

class farmacia(Item):
    nombre=Field()
    precio=Field()

class farmaciaSpider(CrawlSpider):
    name='SpiderFarmacia'
    custom_settings={
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
               
    }
    allowed_domains = ["cruzverde.cl"]
    
    start_urls=["https://www.cruzverde.cl/medicamentos/"]

    rules = (
        Rule(
            #LinkExtractor
            #(
            ##allow=r'start=', 
            #tags=('a', 'at-link','span'), 
            #attrs=('href', 'target',)
            #),
            follow=True, callback="parseFarmacia"
            ),
    )
    download_delay=1

    def parseFarmacia(self, response):
        sel=Selector(response)
        medicamentos=sel.xpath('.//div[@class="col-span-4 lg:col-span-3"]')
        #medicamentos=sel.xpath('.//div[@class="grid grid-cols-1 gap-15 lg:grid-cols-3 lg:gap-30 grid-cols-2"]')

        for medicamento in medicamentos:
            item= ItemLoader(farmacia(),medicamento)
            item.add_xpath('nombre','.//div[@class="relative z-10 mt-5 text-gray-dark flex flex-col flex-1"]//a/span/text()')
            item.add_xpath('precio','.//div[@class="text-12 sm:text-14"]/text()')

            yield item.load_item()

        