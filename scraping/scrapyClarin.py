from scrapy import Field
from scrapy import Item
from scrapy import Spider	
from scrapy import Selector
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess


class Signos(Item):
    titulo= Field()
    descripcion =Field()

class ClarinSpider(Spider):
    name='spiderHoroscopo'
    customer_settings={
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }

    start_urls=['https://www.clarin.com/horoscopo']
    
    def parse(self, response):
        sel=Selector(response)
        lista_signos=sel.xpath('//div[@class="item"]')
        item=ItemLoader(Signos(),lista_signos)
        for signo in lista_signos:
            item=ItemLoader(Signos(),signo)
            item.add_xpath('titulo','.//h2/text()')
            item.add_xpath('descripcion','.//div[@class="description"]//p/text()')

            yield item.load_item()
    

# CORRIENDO SCRAPY SIN LA TERMINAL
process = CrawlerProcess({
    'FEED_FORMAT': 'json',
    'FEED_URI': 'dato_horoscopo.json'
})
process.crawl(ClarinSpider)
process.start()