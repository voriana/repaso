from turtle import delay
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess


class Dpto(Item):
    ubicacion = Field()
    calle = Field()
    barrio = Field()
    provincia = Field()
    superficie = Field()
    ambientes = Field()
    dormitorios = Field()
    expensas = Field()
    montoAlquiler = Field()


class SpiderMercadoLibre(CrawlSpider):
    name = "ArañaAlquileres"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 20

    }

    allowed_domains = ['departamento.mercadolibre.com.ar', 'listado.mercadolibre.com.ar',
                       'inmuebles.mercadolibre.com.ar']

    dominio = "https://listado.mercadolibre.com.ar/"
    busqueda = "alquileres-2-ambientes-capital-federal/"

    start_urls = [dominio + busqueda]

    download_delay = 1

    rules = (
        # regla paginacion
        Rule(
            LinkExtractor(
                allow=r'_Desde_\d+'
            ), follow=True

        ),
        # regla detalla busquedaItem
        Rule(
            LinkExtractor(
                allow=r'/MLA-'
            ), follow=True, callback="Parse_items"

        ),
    )

    def getCalle(self, texto):
        calle = texto.split(",")[0]
        calle = calle.capitalize().strip()
        return calle

    def getBarrio(self, texto):
        barrio = texto.split(",")[1]
        barrio = barrio.capitalize().strip()
        return barrio

    def getProvincia(self, texto):
        provincia = texto.split(",")[-1]
        provincia = provincia.capitalize().strip()
        return provincia

    def Parse_items(self, response):
        item = ItemLoader(Dpto(), response)
        item.add_xpath('ubicacion', '//*[@id="location"]/div/div[1]/div/p/text()')
        item.add_xpath('calle', '//*[@id="location"]/div/div[1]/div/p/text()', MapCompose(self.getCalle))
        item.add_xpath('barrio', '//*[@id="location"]/div/div[1]/div/p/text()', MapCompose(self.getBarrio))
        item.add_xpath('provincia', '//*[@id="location"]/div/div[1]/div/p/text()', MapCompose(self.getProvincia))
        item.add_xpath('superficie', '//*[@id="technical_specifications"]/div/div[1]/table/tbody/tr[2]/td/span/text()')
        item.add_xpath('ambientes', '//*[@id="technical_specifications"]/div/div[1]/table/tbody/tr[3]/td/span/text()')
        item.add_xpath('dormitorios', '//*[@id="technical_specifications"]/div/div[1]/table/tbody/tr[4]/td/span/text()')
        item.add_xpath('expensas', '//*[th="Expensas"]/td/span/text()')
        item.add_xpath('montoAlquiler', '//span[@class="andes-money-amount__fraction"]/text()')

        yield item.load_item()

        #EJECUTAR DESDE CONSOLA
        #scrapy runspider mercadolibre.py - o mercado_libre.json - t json