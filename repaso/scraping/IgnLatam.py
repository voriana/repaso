from calendar import c
from turtle import delay
from urllib import response
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess

"""
tengo que declarar tantas clases como abstracciones quiera hacer
para este caso:
-noticias
-reviews
-videos
"""

class news(Item):
    titulo=Field()
    contenido=Field()

class reviews(Item):
    titulo=Field()
    calificacion=Field()

class videos(Item):
    titulo=Field()
    fechaPublicacion=Field()


class IgnLatamSpider(CrawlSpider):
    name='IGN_SPIDER'

    custom_settings={
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT':60
    }

    allowed_domains=['latam.ign.com']

    download_delay=1

    start_urls=['https://latam.ign.com/se/?model=&q=ps5']

    rules=(

        Rule(
            #regla horizontal por tipo de informacion
            LinkExtractor(
                allow=r'type='
            ),follow=True
        ),
        #regla horizontal por paginacion
        Rule(
            LinkExtractor(
                allow=r'&page=\d+'
            )
        ),
        #reglas verticales para c/items dentro de cada tipo de informacion
        # reviews
        Rule(
            LinkExtractor(
                allow=r'/review/'
            ),follow=True, callback="ParseReviews"
        ),
        #news
        Rule(
            LinkExtractor(
                allow=r'/news/'
            ),follow=True,callback="ParseNews"
        ),
        #videos
        Rule(
            LinkExtractor(
                allow=r'/video/'
            ),follow=True,callback="ParseVideos"
        )
    )

    def quitarEspacios(self, texto):
        nuevotexto= texto.replace("\n","").replace("\t","").replace("\r","").strip()
        return nuevotexto
        #funciones Parse por cada tipo de informacion       
    def ParseReviews(self, response):
        item=ItemLoader(reviews(),response)
        item.add_xpath('titulo','*//h1[@class="strong"]/text()')
        item.add_xpath('calificacion','//span[@class="side-wrapper side-wrapper hexagon-content"]/text()')

        yield item.load_item()

    def ParseVideos(self,response):
        item=ItemLoader(videos(),response)
        item.add_xpath('titulo','//h1[@id="id_title"]/text()')
        item.add_xpath('fechaPublicacion','//span[@class="publish-date"]/text()')
        
        yield item.load_item()
        
    def ParseNews(self,response):
        item=ItemLoader(news(),response)
        item.add_xpath('titulo','//h1[@id="id_title"]/text()')
        item.add_xpath('contenido','//div[@id="id_text"]//*/text()',MapCompose(self.quitarEspacios)) # traeme todos los tag hijos ded id=id_text    

        yield item.load_item()



    