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

# Facebook
def Scraping_Facebook(Urls):
    
    service = Service(r'C:\Users\zorro\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    driver.get("https://www.facebook.com/login/")

    # login

    time.sleep(3)
    username = driver.find_element("css selector", "input[name='email']")
    password = driver.find_element("css selector", "input[name='pass']")
    username.clear()
    password.clear()
    username.send_keys(FACEBOOK_USER)
    password.send_keys(FACEBOOK_PASSWORD)
    driver.find_element("css selector", "button[type='submit']").click()
    time.sleep(6)


    url_list = Urls
    result_list = []

    index = 0
    while index < len(url_list):
        url = url_list[index]
        driver.get(url)
        time.sleep(3)

        Nombre = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div/div/span/h1').text
        Nombre = Nombre.strip()

        seguidores = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/span/a[2]').text
        seguidores = ' '.join(seguidores.split()[:2])

        me_gusta = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/span/a[1]').text
        me_gusta = ' '.join(me_gusta.split()[:2])

        response = {'Nombre': Nombre, 'Seguidores': seguidores, 'Me Gusta': me_gusta}
        result_list.append(response)

        index += 1
    
    print('----------- Facebook ------------ \n')
    print(result_list)
    
    return result_list