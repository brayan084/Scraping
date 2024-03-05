from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# TikToc
def Scraping_TikTok(Urls:list):

    service = Service(r'C:\Users\zorro\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    
    url_list = Urls
    result_list = []

    index = 0
    while index < len(url_list):
        url = url_list[index]
        driver.get(url)
        time.sleep(3)

        Nombre = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/h1').text

        seguidores = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/h3/div[2]/strong').text

        Siguiendo = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/h3/div[1]/strong').text

        Me_Gusta = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/h3/div[3]/strong').text
        
        Descripcion = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/h2').text
        
        response = {'Url': url, 'Nombre': Nombre, 'Seguidores': seguidores, 'Siguiendo': Siguiendo, 'Me Gusta': Me_Gusta, 'Descripcion': Descripcion}
        result_list.append(response)

        index += 1
        
    print('----------- TikTok ------------ \n')
    print(result_list)
    return result_list