import requests
from lxml import html

#headers
header={
    'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
}
#pagina a la que quiero ingresar
url='https://www.github.com/login'

# creo un objeto de tipo sesion (me lo da la lib request) para hacer los request desde aqui
session= requests.session()

res_session= session.get(url=url,headers=header)

#parseo lo que me devuelve la url de login para obtener el token para iniciar sesion
parser= html.fromstring(res_session.text)
auteti_token= parser.xpath('//*[@id="login"]/div[4]/form/input[1]')

login_session='https://github.com/session'
#creo un dic con los datos de body del para enviar al loguearme
archivo= open('D:\cursos\web scraping\loginGit.txt.txt',mode="r")
login= archivo.readline().strip()
passw=archivo.readline().strip()
login_data={
    "login":login,
    "password": passw,
#"login":open('D:\cursos\web scraping\loginGit.txt.txt',mode="r").readline().strip(),
#    "passw":open('D:\cursos\web scraping\loginGit.txt.txt',mode="r").readline().strip(),
    "commit": "Sign in",
    "authenticity_token":auteti_token,
}
session.post(url=login_session,data=login_data,headers=header)


#ahora deberia estar en mis repositorios, para empezar a extraer los datos que quiero
data_url='https://github.com/voriana?tab=repositories'
respuesta= session.get(url=data_url,headers=header)
parser= html.fromstring(respuesta.text)
lista_repo= parser.xpath('//div[1]/div[1]/h3/a/text()')

#recorro los repositorios
for repo in lista_repo:
    print (repo)