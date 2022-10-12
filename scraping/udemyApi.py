import requests
import json

url="https://www.udemy.com/api-2.0/search-courses/?src=ukw&q=python&skip_price=true"

headers={
    "referer": "https://www.udemy.com/courses/search/?src=ukw&q=python",
    "content-type": "application/json; charset=UTF-8"

    
}
response=requests.get(url,headers=headers)
data= response.json()
cursos=data['courses']

#paginacion
paginacion=[5]

for pag in paginacion:
    for curso in cursos:
        print(curso["title"])
        print(curso['num_reviews'])

    