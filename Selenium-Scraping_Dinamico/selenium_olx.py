from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver= webdriver.Edge('./msedgedriver.exe')
driver.get('https://www.olx.com.ar/autos_c378')


for i in range(3):
    try:
        # obtener el elemento boton
        boton=WebDriverWait(driver,9).until(EC.presence_of_element_located(By.XPATH, '//button[@data-aut-id="btnLoadMore"]'))
        boton.click()
        WebDriverWait(driver,10).until(EC.presence_of_all_elements_located(By.XPATH,'//li[@data-aut-id="itemBox"]//span[@data-aut-id="itemPrice"]'))

    except:
        break

#lista de autos de la pagina
autos=driver.find_elements(By.XPATH,'//li[@data-aut-id="itemBox"]')

for auto in autos:
    #obtener precio desde la ruta donde estoy
    precio = auto.find_element(By.XPATH,'.//span[@data-aut-id="itemPrice"]').text
    print(precio)
    descripcion = auto.find_element(By.XPATH,'.//span[@data-aut-id="itemTitle"]').text
    print(descripcion)

