import requests
from lxml import html

url="https://www.wikipedia.org/"

encabezados={
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

response= requests.get(url,headers=encabezados)

parser=html.fromstring(response.text)


#idiomas=parser.xpath('//div[contains(@class,"central-featured-lang")]//strong/text()')
#p# rint(idiomas)

idiomas= parser.find_class("central-featured-lang")
for i in idiomas:
    print(i.text_content())