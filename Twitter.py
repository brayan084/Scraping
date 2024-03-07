from selenium import webdriver
import time
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

load_dotenv()
# Variables de entorno
TWITTER_USER = os.getenv("TWITTER_USER")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

# Twitter
def Scraping_Twitter(Urls:list):
    service = Service(r'C:\Users\zorro\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    
    # login
    
    driver.get("https://twitter.com/login")
    
    time.sleep(3)
    username = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
    username.clear()
    username.send_keys(TWITTER_USER)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span").click()
    time.sleep(3)
    password = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
    password.clear()
    password.send_keys(TWITTER_PASSWORD)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span").click()
    time.sleep(6)

    url_list = Urls
    result_list = []

    index = 0
    while index < len(url_list):
        url = url_list[index]
        time.sleep(2)
                
        if url == 'NO TIENE':
            index += 1
            continue
        
        driver.get(url)
        time.sleep(5)

        try:
            Nombre = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/span/span[1]').text
        except Exception:
            Nombre = 'No hay nombre'
        
        try:
            Seguidores = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span').text
        except Exception:
            Seguidores = 'No hay seguidores'
            
        try:
            Siguiendo = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span').text
        except Exception:
            Siguiendo = 'No hay siguiendo'
            
        try:
            Posts = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div').text
            Posts = Posts.split()
        
            if Posts[1] == 'mil' or Posts[1] == 'mill':
                Posts = ' '.join(Posts[:2])
            else: 
                Posts = ' '.join(Posts[:1])
        except Exception:
            Posts = 'No hay posts'
            
        response = {'Url': url, 'Nombre': Nombre, 'Seguidores': Seguidores, 'Siguiendo': Siguiendo, 'Posts': Posts}
        result_list.append(response)

        index += 1

    print('----------- Twitter ------------ \n')
    print(result_list)

    return result_list