
from scrapy.selector import Selector
from scrapy.spiders import Spider
from scrapy.crawler import CrawlerProcess
import scrapy

class LoginSpider(Spider):
    name='GithubLogin'
    starts_url=['https://github.com/login']
    #credenciales=open("D:\cursos\web scraping\loginGit.txt")
    #user= credenciales.readline().strip()
    #token= credenciales.readline().strip()   #funcion de scrapy para mandar un formulario de login
    
    def parse(self,response):
        credenciales=open("D:\cursos\web scraping\credenciales.txt")
        user= credenciales.readline().strip()
        token= credenciales.readline().strip()

        return scrapy.FormRequest.from_response(
            response,
            formdata={
            'login': user,
            'password': token,

        },
        callaback=self.after_login
        )
    
    def after_login(self,response):
        request=scrapy.Request(
            url='https://github.com/voriana?tab=repositories',
            callback=self.parse_repositorios
        )
        yield request
    
    def parse_repositorios(self,response):
        sel=Selector(response)
        repositorios= sel.xpath('//div[1]/div[1]/h3/a/text()')
        for repo in repositorios:
            print(repo.get())
            
process=CrawlerProcess()
process.crawl(LoginSpider)
process.start()
