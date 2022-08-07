
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess



#crear clase principal
class Alquileres(Item):

    #atributos de esta clase--> que campos quiero obtener
    zona= Field()
    calle=Field()
    precio=Field()
    tipoMoneda=Field()
    habitaciones=Field()
    expensas=Field()
    piso=Field()
    m2=Field()

class AlquilerSpider(CrawlSpider):
    name="OrianaAlquileres"

    custom_settings={
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
    }
    dominio='https://www.argenprop.com'

    start_urls=[dominio+'/departamento-alquiler-2-ambientes']

    download_delay=2

    rules=(
        Rule(
            LinkExtractor(
                allow=dominio+r'/departamento-en-alquiler-en-' ##exp. regular que accede a las urls que cumplan con este parametro
            ),follow=True,callback="parseAlquiler"
        ),
            
    )

    def quitarEspacios(self, texto):
        nuevoTexto= (texto.replace('\n','')).strip()
        return nuevoTexto

    def obtenerMoneda(self,texto):
        moneda=self.quitarEspacios(texto)[0]
        return moneda
    
    def getFinalTexto(self,texto):
        nuevo_texto=texto.split(",")[-1]
        nuevo_texto=nuevo_texto.capitalize().strip()
        return nuevo_texto
    
    def getInicioTexto(self,texto):
        calle=texto.split(",")[0]
        calle=calle.capitalize().strip()
        return calle
    
    
   

    def parseAlquiler(self,response):
        sel=Selector(response)
        item=ItemLoader(Alquileres(),sel)     
        item.add_xpath('zona','//div/h2/text()',MapCompose(self.getFinalTexto) )
        item.add_xpath('calle','//div/h3/text()',MapCompose(self.getInicioTexto))
        item.add_xpath('piso','//div/h3/text()',MapCompose(self.getFinalTexto)) 
        item.add_xpath('m2','///ul/li[1]/div/p[2]/text()')
        item.add_xpath('precio','//p[@class="titlebar__price"]/text()',MapCompose(self.quitarEspacios))
        item.add_xpath('tipoMoneda','//p[@class="titlebar__price"]/text()',MapCompose(self.obtenerMoneda)) 
        item.add_xpath('habitaciones','//*[@id="section_1"]/li[1]/p/strong/text()',MapCompose(self.quitarEspacios)) #esta tambien funciona //section/ul[@id="section_1" and @class="property-features"]/li/p/strong
        item.add_xpath('expensas','//*[@id="section_1"]/li[9]/p/strong/text()',MapCompose(self.quitarEspacios))
        #item.add_xpath('requisitos','')

        yield item.load_item()


# CORRIENDO SCRAPY SIN LA TERMINAL
#process = CrawlerProcess({
#     'FEED_FORMAT': 'csv',
#     'FEED_URI': 'archivo_alquileres.csv'
# })
#process.crawl(AlquilerSpider)
#process.start()

    

