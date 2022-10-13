import requests
import json



headers={
    "referer": "https://www.udemy.com/courses/search/?src=ukw&q=python",
    "content-type": "application/json; charset=UTF-8"
}

#paginacion
for i in range(1,4):
    url="https://www.udemy.com/api-2.0/search-courses/?src=ukw&q=python&skip_price=true&p="+str(i)
    response=requests.get(url,headers=headers)
    data= response.json()
    cursos=data['courses']

    for curso in cursos:
        print('title '+curso["title"])
        print('reviews '+str(curso['num_reviews']))
        print('rating' +str(curso['rating']))
        print()

    