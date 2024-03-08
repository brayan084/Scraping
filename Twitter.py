from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Twitter
def Scraping_Twitter(Urls:list):
    service = Service(r'C:\Users\zorro\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    
    # start_time = time.time()
    driver.get("https://twitter.com/apify")

    
    url_list = Urls
    result_list = []

    index = 0
    while index < len(url_list):
        url = url_list[index]
        time.sleep(6)
                
        if url == 'NO TIENE':
            index += 1
            continue
        
        # start_time1 = time.time()
        driver.get(url)
        try:
            # lo que hace esto es basicamente es esperar a que se carguen los datos que buscamos y hay sigue ejecutandoce
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span")))
                
        except Exception:
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/h2/div/div/div/div/span[1]/span/span[1]")))
            except Exception:
                response_404 = {'Url': url, 'Nombre': 'No hay nombre', 'Seguidores': 'No hay seguidores', 'Siguiendo': 'No hay siguiendo', 'Posts': 'No hay posts'}
                result_list.append(response_404)
                # print(response_404)
                index += 1
                continue
                

        try:
            Nombre = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/span/span[1]').text
        except Exception:
            try:
                Nombre = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/h2/div/div/div/div/span[1]/span/span[1]').text
            except Exception:
                Nombre = 'No hay nombre'
        
        try:
            Seguidores = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span').text
        except Exception:
            try:
                Seguidores = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div[1]/div/div[5]/div[2]/div/span[1]/span').text
            except Exception:
                Seguidores = 'No hay seguidores'
            
        try:
            Siguiendo = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span').text
        except Exception:
            try:
                Siguiendo = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div[1]/div/div[5]/div[1]/div/span[1]/span').text
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
            # try:
            #     Posts = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div').text
            #     Posts = Posts.split()
            
            #     if Posts[1] == 'mil' or Posts[1] == 'mill':
            #         Posts = ' '.join(Posts[:2])
            #     else: 
            #         Posts = ' '.join(Posts[:1])
            # except Exception:
            Posts = 'No hay posts'
            
            
        response = {'Url': url, 'Nombre': Nombre, 'Seguidores': Seguidores, 'Siguiendo': Siguiendo, 'Posts': Posts}
        # print(response)
        result_list.append(response)

        index += 1

        
        
    print('----------- Twitter ------------ \n')
    # print(result_list)

    return result_list