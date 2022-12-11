import requests
import json


endpoint="https://api.github.com/user/repos"
credenciales=open('D:\cursos\web scraping\webscraping autenticacion y catchas\credenciales.txt',mode='r')
usuario=credenciales.readline().strip()

#ahora github necesita OAuth desde la web obtuve el personal token, ver como se podria generar dinamicamente
token="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"

response=requests.get(url=endpoint,auth=(usuario,token))
#print(json.dumps(response.json(),indent=4))
repositorios= response.json()
for repo in repositorios:
    print(repo['name'])