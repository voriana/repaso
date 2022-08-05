
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
    precio=Field()
    cantAmb=Field()
    #expensas=Field()
    #requesitos=Field()

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

    def parseAlquiler(self,response):
        sel=Selector(response)
        item=ItemLoader(Alquileres(),sel)

        item.add_xpath('zona','//div/h3/text()') #/html/body/main/div[1]/div[1]/div[3]/div[4]/section[3]/p[2]/text()
        item.add_xpath('precio','//p[@class="titlebar__price"]/text()') #//*[@id="section_2"]/li[3]/p/strong/text()
        item.add_xpath('cantAmb','/html/body/main/div[1]/div[1]/div[3]/div[4]/ul/li[1]/div/p[2]/text()')
        #item.add_xpath('expensas','')
        #item.add_xpath('requisitos','')

        yield item.load_item()

# CORRIENDO SCRAPY SIN LA TERMINAL
#process = CrawlerProcess({
#     'FEED_FORMAT': 'csv',
#     'FEED_URI': 'archivo_alquileres.csv'
# })
#process.crawl(AlquilerSpider)
#process.start()

    

