from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# instagram
def Scraping_Instagram(Urls:list):
    
    service = Service(r'C:\Users\zorro\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()    

    driver.get("https://www.instagram.com/theofficialpandora/")
    time.sleep(6)
    
    # si la ip es de estados unidos tiene que estar comentado esto
    driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]').click()
    time.sleep(1)

    url_list_ig = Urls
    result_list_ig = []

    index_ig = 0
    while index_ig < len(url_list_ig):
        url = url_list_ig[index_ig]
        time.sleep(2)
                
        if url == 'NO TIENE':
            index_ig += 1
            continue
        
        driver.get(url)
        time.sleep(3)
        try:
            Nombre = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[1]/h2').text
            # print(Nombre)
        except Exception:
            Nombre = 'No hay nombre'
        try:
            seguidores = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span/span').text
            # print(seguidores)
        except Exception:
            seguidores = 'No hay seguidores'
        try:
            Seguidos = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button/span/span').text
            # print(Seguidos)
        except Exception:
            Seguidos = 'No hay seguidos'
        try:
            Publicaciones = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[1]/button/span/span').text
            # print(Publicaciones)
        except Exception:
            Publicaciones = 'No hay publicaciones'

        
        
        response = {'Url': url, 'Nombre': Nombre, 'Seguidores': seguidores, 'Seguidos': Seguidos, 'Publicaciones': Publicaciones}
        print(response)
        result_list_ig.append(response)

        index_ig += 1
        
    print('----------- Instagram ------------ \n')
    print(result_list_ig)
    
    return result_list_ig
