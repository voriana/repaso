from scrapy import Field
from scrapy import Item
from scrapy import Spider	
from scrapy import Selector
from scrapy.loader import ItemLoader

class Preguntas(Item):
    pregunta=Field()
    #descripcion=Field()

    

class StackOverflowSpider(Spider):
    name='OrianaSpider'

    customer_settings={
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }
    starts_url='https://stackoverflow.com/questions'

    def parse(self, response):
        elemento_seleccionado=Selector(response)
        preg_arbol_html=elemento_seleccionado.xpath('//div[@id=questions]//div[@class="s-post-summary js-post-summary"]')

        for pregunta in preg_arbol_html:
            item=ItemLoader(Preguntas(),pregunta)
            item.add_xpath('pregunta','.//h3/a/text()')
            #item.add_xpath('descripcion','.//div[@class="s-post-summary--content-excerpt"]/text()')

            yield item.load_item()

