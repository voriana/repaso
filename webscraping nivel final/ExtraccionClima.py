from twisted.internet import reactor
from twisted.internet.task import LoopingCall
from scrapy.crawler import CrawlerRunner
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider

# CREO LA CLASE QUE VA HACER LA EXTRACCION
class ExtraccionClima(Spider):
    name= "CLIMA"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 20,
        'LOG_ENABLED': True # Elimina los miles de logs que salen al ejecutar Scrapy en terminal
    }

    #LAS URL POR CADA CIUDAD QUE SE QUIERE TENER EL CLIMA
    start_urls=[
        "https://www.accuweather.com/es/ar/buenos-aires/7894/weather-forecast/7894",
        "https://www.accuweather.com/es/ar/c%C3%B3rdoba/8869/weather-forecast/8869",
        "https://www.accuweather.com/es/ar/santa-f%C3%A9/11221/weather-forecast/11221"
    ]

    #funcion para hacer el parser
    def parse(self, response):
        ciudad= response.xpath('//h1/text()').get()
        current=response.xpath('//div[@class="cur-con-weather-card__panel"]//div[@class="temp"]/text()').get()
        real_feel=response.xpath('//div[@class="cur-con-weather-card__panel"]//div[@class="real-feel"]/text()').get()

        ciudad=ciudad.split(',')[-1].strip()
        current= current.replace('°','').replace('\n','').replace('\r','').strip()
        real_feel= real_feel.replace('RealFeel®','').replace('\n','').replace('\r','').strip()

        print(ciudad)
        print(current)
        print(real_feel)

        f=open("./datos_clima_scrapy.csv","a")
        f.write(ciudad+','+current+','+real_feel+'\n')
        f.close()
    
process=CrawlerProcess()
process.crawl(ExtraccionClima)
process.start()
#programacion de ejecucion periodicamente
#runner= CrawlerRunner()
#task= LoopingCall(lambda:runner.crawl(ExtraccionClima))
#task.start(20)# cada hora, esto esta expresado en segundos
#reactor.run()
