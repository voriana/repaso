from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup


class Opinion(Item):
    autor=Field()
    titulo=Field()
    contenido=Field()
    calificacion=Field()
    

class TripAdvisor(CrawlSpider):
    name="TripAdvisorSpider"
    custom_settings={
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        "Connection": "keep-alive",
        'CLOSESPIDER_PAGECOUNT': 100 # Un poco alto
    }
    download_delay=1
    
    allowed_domains=['tripadvisor.com.ar','tripadvisor.com']
    start_urls=["https://www.tripadvisor.com.ar/Hotels-g297478-Medellin_Antioquia_Department-Hotels.html"]

    rules=(
        #regla paginacion hoteles (horizontal)
        Rule(
            LinkExtractor(
                allow=r'-oa\d+-'
            ),follow=True

        ),
        #regla vertical hoteles
        Rule(
            LinkExtractor(
                allow=r'/Hotel_Review-',restrict_xpaths=['*//a[@data-clicksource="HotelName"]']
            ),follow=True

        ),
        #regla paginacion horizontal opiniones dentro de un  hoteles
        Rule(
            LinkExtractor(
                allow=r'-or\d+-'
            ),follow=True

        ),
        #regla perfiles de  usuarios vertical
        Rule(
            LinkExtractor(
                allow=r'/Profile/', restrict_xpaths=['//div[@data-test-target="reviews-tab"]//a[contains(@class,"ui_header")]']
            ),follow=True,callback='ParseOpinion'

        ),
        Rule(

        )
    )

    def obtenerCalificacion(self, texto):
        calificacion=texto.split("_")[-1]
        return calificacion



    def ParseOpinion(self,response):
        sel=Selector(self, response)
        Opiniones=[sel.xpath('//div[@id="content"]/div/div')]
        autor=sel.xpath('//h1/span/text()').get()

        #obtengo los datos que necesito de cada opinion
        for opinion in Opiniones:
            item=ItemLoader(Opinion(),opinion)
            item._add_value('autor',autor)
            item.add_xpath('titulo','//div[@class="muQub VrCoN"]/div[1]/text()')
            item.add_xpath('contenido','//q/text()')
            item.add_xpath('calificacion','//a/div/span[contains(@class,"ui_bubble")]/text()',MapCompose(self.obtenerCalificacion))
            

            yield item.load_item()
            
