from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess

class Deportes(Item):
    titular=Field()
    descripcion=Field()

class DeportesSpider(Spider):
    name='Spider Clarin Deportes'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        # 'FEED_EXPORT_FIELDS': ['id', 'descripcion', 'titular'], # Como ordenar las columnas en el CSV?
        # 'CONCURRENT_REQUESTS': 1 # numero de requerimientos concurrentes 
        #'FEED_EXPORT_ENCODING': 'utf-8'
    }
    start_urls=["https://www.clarin.com/deportes/"]

    def parse(self, response, **kwargs):
        soup=BeautifulSoup(response.body)
        contenedor_noticias= soup.find_all(class_="content-nota onexone_foto list")

        for contenedor in contenedor_noticias:
            noticias=contenedor.find_all(class_="mt",recursive=False)

            for noticia in noticias:
                item = ItemLoader(Deportes(), response.body)
                titular =  noticia.find('p')
                descripcion=noticia.find('h2').text.replace('\n', '').replace('\r', '')

                item.add_value('titular', titular)
                item.add_value('descripcion', descripcion)
                descripcion = noticia.find('p')
                if (descripcion):
                  item.add_value('descripcion', descripcion.text.replace('\n', '').replace('\r', ''))
                else:
                  item.add_value('descripcion', 'N/A')

                yield item.load_item()
# CORRIENDO SCRAPY SIN LA TERMINAL
process = CrawlerProcess({
     'FEED_FORMAT': 'json',
     'FEED_URI': 'deportes_Clarin.json'
 })
process.crawl(DeportesSpider)
process.start()