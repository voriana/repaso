import schedule
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


start_urls=[
    "https://www.accuweather.com/es/ar/buenos-aires/7894/weather-forecast/7894",
    "https://www.accuweather.com/es/ar/c%C3%B3rdoba/8869/weather-forecast/8869",
    "https://www.accuweather.com/es/ar/santa-f%C3%A9/11221/weather-forecast/11221"
]

def extraer_datos():
    driver= webdriver.Chrome('D:\\cursos\\web scraping\\webscraping nivel final\\chromedriver_win32\\chromedriver.exe')
    
    for url in start_urls:
        driver.get(url)

        ciudad=driver.find_element(By.XPATH,'//h1').text
        current=driver.find_element(By.XPATH,'//div[@class="cur-con-weather-card__panel"]//div[@class="temp"]').text
        real_feel=driver.find_element(By.XPATH,'//div[@class="cur-con-weather-card__panel"]//div[@class="real-feel"]').text

        # Limpieza de datos
        ciudad = ciudad.replace('\n', '').replace('\r', '').strip()
        current = current.replace('°', '').replace('\n', '').replace('\r', '').strip()
        real_feel = real_feel.replace('RealFeel®', '').replace('°', '').replace('\n', '').replace('\r', '').strip()
        
        # Guardado de datos en un archivo
        f = open("./datos_clima_selenium.csv", "a")
        f.write(ciudad + "," + current + "," + real_feel + "\n")
        f.close()
        print(ciudad)
        print(current)
        print(real_feel)
        print()

    driver.close()
