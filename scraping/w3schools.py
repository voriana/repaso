from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy import Request

class Dummy(Item):
    titulo =Field()
    titulo_iframe=Field()


#clase corde la que gace el scrapy
class w3SCrawler(CrawlSpider):
    name='W3SC'

    custom_settings={
    "user-agent ": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
     'REDIRECT_ENABLED': True
    }

    allowed_domains=['w3schools.com']
    start_urls=["https://www.w3schools.com/html/html_iframe.asp"]
    
    download_delay=2

    def parse(self,response):
        sel=Selector(response)
        titulo=sel.xpath('//div[@id="main"]//h1/span/text()').get() 
        meta_data={'titulo':titulo}
        
        #iframe_url=sel.xpath('//div[@id="main"]//iframe[@width="99%"]/@src').get()
        iframe_url1=sel.xpath('//div//iframe[@title="W3Schools HTML Tutorial"]/@src').get

        iframe_url='https://www.w3schools.com/html/' + iframe_url1

        yield Request(iframe_url,callback = self.parse_iframe,meta = meta_data)

    def parse_iframe (self,response):
        item= ItemLoader(Dummy(),response)
        item.add_xpath('titulo_iframe','//div[@id="main"]//h1/span/text()')
        item.add_value('titulo',response.meta.get('titulo'))
        
        yield item.load_item()
 

    # CORRIENDO SCRAPY SIN LA TERMINAL
 