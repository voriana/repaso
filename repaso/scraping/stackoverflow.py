from urllib import response
import requests
from bs4 import  BeautifulSoup

headers={
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
url="https://stackoverflow.com/questions"

response=requests.get(url,headers=headers)

#es un parseador 
soup= BeautifulSoup(response.text,features="lxml")

contenedor_de_preguntas=soup.find('div',id="questions")

lista_de_preguntas=contenedor_de_preguntas.find_all('div',class_="s-post-summary js-post-summary")

for pregunta in lista_de_preguntas:
    
    elemento_pregunta=pregunta.find('h3')
    texto_pregunta=elemento_pregunta.text
    
    #contenido_preg=pregunta.find(class_="s-post-summary--content-excerpt").text
    contenido_preg=elemento_pregunta.find_next_sibling('div').text
    contenido_preg=contenido_preg.replace('\n','').replace('\r','').strip()
    print(texto_pregunta)
    print(contenido_preg+'\n')

