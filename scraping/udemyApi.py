import requests
import json
import pandas as pd

curso_totales=[]

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
        curso_totales.append({
            'title ':curso["title"],
            'reviews ': str(curso['num_reviews']),
            'rating' : str(curso['rating'])
        })



df=pd.DataFrame(curso_totales)
print(df)
df.to_csv('cursosUdemy.csv')
    

    