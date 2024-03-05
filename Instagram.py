from selenium import webdriver
import time
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


load_dotenv()
# Variables de entorno
FACEBOOK_USER = os.getenv("FACEBOOK_USER")
FACEBOOK_PASSWORD = os.getenv("FACEBOOK_PASSWORD")


# instagram
def Scraping_Instagram(Urls:list):
    
    service = Service(r'C:\Users\zorro\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()    

    driver.get("https://www.instagram.com/accounts/login/")

    # login
    time.sleep(3)
    usernameIG = driver.find_element("css selector", "input[name='username']")
    passwordIG = driver.find_element("css selector", "input[name='password']")
    usernameIG.clear()
    passwordIG.clear()
    usernameIG.send_keys(FACEBOOK_USER)
    passwordIG.send_keys(FACEBOOK_PASSWORD)
    driver.find_element("css selector", "button[type='submit']").click()
    time.sleep(6)

    url_list_ig = Urls
    result_list_ig = []

    index_ig = 0
    while index_ig < len(url_list_ig):
        url = url_list_ig[index_ig]
        driver.get(url)
        time.sleep(3)

        Nombre = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/a/h2').text
        # print(Nombre)

        seguidores = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span/span').text
        # print(seguidores)

        Seguidos = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a/span/span').text
        # print(Seguidos)

        Publicaciones = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[1]/span/span').text
        # print(Publicaciones)
        
        
        response = {'Nombre': Nombre, 'Seguidores': seguidores, 'Seguidos': Seguidos, 'Publicaciones': Publicaciones}
        result_list_ig.append(response)

        index_ig += 1
        
    print('----------- Instagram ------------ \n')
    print(result_list_ig)
    
    return result_list_ig